import re

# findall
# * - stands for 0 or more instances
print(re.findall("ab*c", "ac"))
print(re.findall("ab*c", "abcd"))
print(re.findall("ab*c", "acc"))
print(re.findall("ab*c", "abcac"))
print(re.findall("ab*c", "abdc"))

# ignore case with re.IGNORECASE
print('\n--- Ignoring case ---')
print(re.findall("ab*c", "ABC"))
print(re.findall("ab*c", "ABC", re.IGNORECASE))

# period(.) - stands for any single character
print(
    "\n--- Period(.) ---", "\n",
    re.findall("a.c", "abc"), "\n",
    re.findall("a.c", "abbc"), "\n",
    re.findall("a.c", "ac"), "\n",
    re.findall("a.c", "acc")
)

# The pattern .* inside a regular expression stands
# for any character repeated any number of times.
# For instance, you can use "a.*c" to find every
# substring that starts with "a" and ends with "c",
# regardless of which letter—or letters—are in between:

find_this = "a.*c"
print(
    "\n--- Pattern(.*) ---\n",
    re.findall(find_this, "abc"), "\n",
    re.findall(find_this, "abbc"), "\n",
    re.findall(find_this, "ac"), "\n",
    re.findall(find_this, "acc"), "\n"
)

# match_results
match_result = re.search("ab*c", "ABC", re.IGNORECASE)
print(
    "\n--- match_result ---\n",
    match_result.group()
)

# re.sub()
string = "Everything is <replaced> if it's in <tags>."
# string = re.sub("<.*>", "ELEPHANTS", string)
# string = re.sub("<.*?>", "GIRAFFE", string)
# print(string)

print(
    re.sub("<.*>", "ELEPHANTS", string), "\n",
    re.sub("<.*?>", "GIRAFFE", string)
)