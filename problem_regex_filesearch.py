import os
import re
import operator

CHARACTERS_FOR_NEAR = 80
CHARACTERS_FOR_WILDCARD = 160

# analyzes files matching filespec (recursively) using criteria given in searchdictionary
def analyze_files(path, filespec, searchdictionary):
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
            pattern = rereplace.sub(".{1,"+str(CHARACTERS_FOR_NEAR)+"}", pattern)

            # replace all spaces with \s+
            rereplace = re.compile(" ")
            pattern = rereplace.sub(r"\s+", pattern)

            # replace all occurrences of '.*' with .{1,CHARACTERS_FOR_WILDCARD}
            rereplace = re.compile("\.\*")
            pattern = rereplace.sub(".{1,"+str(CHARACTERS_FOR_WILDCARD)+"}", pattern)

            pat = re.compile(pattern, re.MULTILINE | re.IGNORECASE)
            reres = pat.findall(contents)
            if len(reres):
                print("\nMatches for searchstring:", pattern)
                for i in reres:
                    print(i)
                print("\n")
            matchcount += len(reres)

        return matchcount * float(searchvalue)

    def analyze_file(filename):
        print(filename)
        with open(filename, "rt") as file:
            contents = " ".join(line.strip() for line in file)

        res = 0
        for searchkey, searchvalue in searchdictionary.items():
            res += get_search_result(contents, searchkey, searchvalue)
            print(searchkey, ":", res)

        return {filename: res}

    result = {}
    for root, dirs, files in os.walk(path):
        # filter out files not matching filespec
        files = list(filter(lambda x: re.search(filespec, x), files))
        for name in files:
            filename = os.path.join(root, name)
            res = analyze_file(filename)
            if any(res.values()):
                result.update(res)

    return result


def text_analysis():
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

    searchdictionary = {r"(testname|derek) NEAR (def)": 0.1, r"import \bre\b": 0.1, r"isinstance NEAR TypeError": 10, r"def NEAR if": 5}
    searchdictionary = {r"import \bre\b": 0.1}
    result = analyze_files('c:\\dev\\python\\textdatabase\\', ".*py", searchdictionary)

    sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)

    for i in sorted_result:
        print("{} : {:.2f}".format(i[0], i[1]))
