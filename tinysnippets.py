#-*- coding: utf-8 -*-
# tinysnippets.py  (c)2021  Henrique Moreira

"""
Shows sub-modules listed at .gitmodules, to be added on README.md
"""

# pylint: disable=missing-docstring

import sys

def main():
    """ Main function """
    run(sys.argv[1:])

def run(args:list) -> int:
    fname = args[0] if args else ".gitmodules"
    if len(args) > 1:
        return -1
    git_modules_fname = fname
    within = "git submodule add "
    astr, _ = dump_subs("""
## Log history

Original [github](https://github.com/) repo [here](https://github.com/serrasqueiro/tiny-snippets/).

Here are the list of historical adds.
""", within, git_modules_fname, sys.stderr)
    if not astr:
        return 2
    print(astr)
    return 0

def dump_subs(pre:str, within:str, fname:str, out) -> tuple:
    """ Returns a pair:
        - complete git add module lines
        - sub-modules
    """
    astr = pre
    subs = ""
    last = ""
    blanked = " " * 3
    for aline in open(fname, "r").readlines():
        line = aline.strip()
        if line.startswith("["):	# [submodule "abc/def"]
            last = ""
            continue
        if line.startswith("path = "):
            last = line.split("path =", maxsplit=1)[1].strip()
        pos = line.find("url = ")
        if pos < 0:
            continue
        rest = line.split("url = ", maxsplit=1)[1].strip()
        dock = rest.split(":")[-1].split(".git")[0]
        sub = f" {last}" if last else ""
        s_url = f"[{better_path(last)}](https://gist.github.com/serrasqueiro/{dock})"
        if s_url:
            s_url = s_url + f",\n{blanked}+ "
        astr += f"1. {s_url}`" + within + rest + sub + "`\n"
        subs += rest + "\n"
        if out:
            out.write(f"{line}\n")
    tup = (astr, subs)
    return tup

def better_path(astr:str) -> str:
    result = astr.replace("_", " ")
    return result

if __name__=="__main__":
    main()
