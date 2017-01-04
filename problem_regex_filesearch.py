import os
import re
import operator
from multiprocessing import Pool, Process, Value, Array
from itertools import repeat

CHARACTERS_FOR_NEAR = 80
CHARACTERS_FOR_WILDCARD = 160
CHARACTERS_FOR_MATCH_EXTRACTION = 50

THREADS_FOR_ANALYSES = 8


def debugprint(*args):
    # print(*args)
    pass

def get_search_result(contents, searchkey, searchvalue):

    patterns = searchkey.split(";")
    # print(patterns)
    matchcount = 0
    for pattern in patterns:
        # if there are groups, change them to non-capturing (to be able to print the whole match during debugging)
        # replace ( with (?:
        rereplace = re.compile("\(")
        pattern = rereplace.sub("(?:", pattern)

        # replace Keyword NEAR with .{1,CHARACTERS_FOR_NEAR}
        rereplace = re.compile(" NEAR ")
        pattern = rereplace.sub(".{1," + str(CHARACTERS_FOR_NEAR) + "}", pattern)

        # replace all spaces with \s+
        rereplace = re.compile(" ")
        pattern = rereplace.sub(r"\s+", pattern)

        # replace all occurrences of '.*' with .{1,CHARACTERS_FOR_WILDCARD}
        rereplace = re.compile("\.\*")
        pattern = rereplace.sub(".{1," + str(CHARACTERS_FOR_WILDCARD) + "}", pattern)

        pat = re.compile(pattern, re.MULTILINE | re.IGNORECASE)
        reres = pat.findall(contents)

        if len(reres):
            debugprint("\nMatches for searchstring:", pattern)
            # recompile pattern to extract surrounding text for display of match
            pat = re.compile(".{1," + str(CHARACTERS_FOR_MATCH_EXTRACTION) + "}" + pattern + \
                             ".{1," + str(CHARACTERS_FOR_MATCH_EXTRACTION) + "}", re.MULTILINE | re.IGNORECASE)
            reres = pat.findall(contents)
            for i in reres:
                print(i)
        matchcount += len(reres)

    return matchcount * float(searchvalue)


def analyze_file(filename, searchdictionary):
    debugprint(filename)
    with open(filename, "rb") as file:
        contents = " ".join(str(line).strip() for line in file)

    res = 0
    for searchkey, searchvalue in searchdictionary.items():
        res += get_search_result(contents, searchkey, searchvalue)
        debugprint(searchkey, ":", res)

    result = {filename: res}
    return result


# analyzes files matching filespec (recursively) using criteria given in searchdictionary
def analyze_files(path, filespec, searchdictionary):

    result = {}
    filecount = 0
    filenames = []

    # first, collect all filenames to work on
    for root, dirs, files in os.walk(path):
        # filter out files not matching filespec
        files = list(filter(lambda x: re.search(filespec, x), files))
        for name in files:
            filename = os.path.join(root, name)
            filenames.append(filename)
            filecount += 1

    # then span the search threads
    with Pool(THREADS_FOR_ANALYSES) as thread_pool:
        res = thread_pool.starmap(analyze_file, zip(filenames, repeat(searchdictionary)))
        thread_pool.close()
        thread_pool.join()
        for i in res:
            result.update(i)

    return result


def import_search_patterns(searchdirectoy):
    result = {}
    with open(searchdirectoy, "rt") as file:
        for line in file:
            line = line.strip()
            if len(line) == 0 or line[0] == '#':
                continue

            searchweight, pattern = line.split(" ", maxsplit=1)
            result[pattern] = float(searchweight)

        # print("\nSearchpattern and weights:")
        # print(result)
        # print("\n")
        return result


def text_analysis(root_search_path=""):
    '''
    important infors about regex spec:
        - all matches are case insensitve and multi-line
        - Keyword NEAR: is replaced with .*{1,CHARACTERS_FOR_NEAR}
        - all single spaces are replaced with any amount of spaces \s+
        - \b can be used to mark word boundaries (\bre\b) will only match ' re ' and not e.g. 'result'
        - alternatives can be expressed using (one|two) -> will match either 'one' or 'two'
          (will be converted to non-capturing groups -> (?:one|two)
        - all occurrences '.*' will be replaced with {} .{1,CHARACTERS_FOR_WILDCARD}
    '''

    if len(root_search_path) == 0:
        root_search_path = r"r:/1/"

    # searchdictionary = {r"(testname|derek) NEAR (def)": 0.1, r"import \bre\b": 0.1, r"isinstance NEAR TypeError": 10, r"def NEAR if": 5}
    # searchdictionary = {r"CacheDispatcher\bThread\b": 1, r"CacheDispatcher": .5}

    searchdictionary = import_search_patterns(r'r:/1/searchdefinitions.txt')

    result = analyze_files(root_search_path, r"(txt|TXT|java)$", searchdictionary)
    sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)

    for i in sorted_result:
        print("{} : {:.2f}".format(i[0], i[1]))
