#-*- coding: utf-8 -*-
# tinysnippets.py  (c)2021  Henrique Moreira

"""
Shows sub-modules listed at .gitmodules, to be added on README.md
"""

# pylint: disable=missing-docstring

import sys
import os.path

SHOW_NEW_ONLY = True

EXCLUDE_COMPLAIN_ON = (
    "misc/keepit",
    "snippets/links",
    "debmin",
    "serrasqueiro/jogaemcasa",
)


def main():
    """ Main function """
    run(sys.argv[1:])

def run(args:list) -> int:
    """ Main script """
    hashes = hashes_there()
    fname = args[0] if args else ".gitmodules"
    if len(args) > 1:
        return -1
    git_modules_fname = fname
    within = "git submodule add "
    news, astr, _ = dump_subs(hashes, """
## Log history

Original [github](https://github.com/) repo [here](https://github.com/serrasqueiro/tiny-snippets/).

Here are the list of historical adds.
""", within, git_modules_fname, sys.stderr)
    if not astr:
        return 2
    if SHOW_NEW_ONLY:
        print(news)
    else:
        print(astr)
    return 0

def dump_subs(hashes, pre:str, within:str, fname:str, out) -> tuple:
    """ Returns a pair:
        - complete git add module lines
        - sub-modules
    """
    assert hashes
    exc_these = EXCLUDE_COMPLAIN_ON
    astr = pre
    news, subs = "", ""
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
        astring = f"1. {s_url}`" + within + rest + sub + "`\n"
        # If any of specific strings found, do nothing:
        if [item for item in exc_these if item in astring]:
            #print("@@@", astring.replace("\n", "~"))
            astring = ""
        astr += astring
        if rest in hashes:
            # The line already exists
            pass
        else:
            news += astring
        subs += rest + "\n"
        if out:
            out.write(f"{line}\n")
    return (news, astr, subs)

def better_path(astr:str) -> str:
    result = astr.replace("_", " ")
    return result

def hashes_there(fname:str=""):
    magic_str = "git@gist.github.com:"
    path = fname if fname else "README.md"
    lines = open(path, "r", encoding="ISO-8859-1").read().splitlines()
    hashes = []
    last = ""
    for line in lines:
        if magic_str not in line:
            last = line
            continue
        a_hash = line.split(":", maxsplit=1)[1].split(" ")[0]
        assert a_hash
        assert last.startswith("1. ["), f"Invalid last: '{last}'"
        sub_dir = last[len("1. ["):].split("]")[0].replace(" ", "_")
        if not os.path.isdir(sub_dir):
            print("#Warn:", "Not a sub dir:", sub_dir)
        hashes.append(magic_str + a_hash)
        last = line
    return hashes


if __name__=="__main__":
    main()
