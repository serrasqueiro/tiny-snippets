#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# tinysnippets.py  (c)2021 .. 2024  Henrique Moreira

"""
Shows sub-modules listed at .gitmodules, to be added on README.md
"""

# pylint: disable=missing-docstring, too-many-locals

import sys
import os.path

DEBUG = 0
SHOW_NEW_ONLY = True

IO_FILE = "README.md"

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
    hashes = hashes_there(debug=DEBUG)
    if DEBUG > 0:
        print('\n'.join(['# +++ ' + ala for ala in hashes]), end="\n++++\n\n")
    fname = args[0] if args else ".gitmodules"
    if len(args) > 1:
        return -1
    git_modules_fname = fname
    within = "git submodule add "
    news, astr, _ = dump_subs(
        hashes, """
## Log history

Original [github](https://github.com/) repo [here](https://github.com/serrasqueiro/tiny-snippets/).

Here are the list of historical adds.
""",
        within,
        git_modules_fname,
        debug=DEBUG
    )
    if not astr:
        return 2
    if SHOW_NEW_ONLY:
        print(news)
        # Appending README.md file
        if news:
            print("#	New lines at {}: {}".format(IO_FILE, news.count('\n')))
        did = append_data(news)
    else:
        print(astr)
    return 0

def dump_subs(hashes, pre:str, within:str, fname:str, debug=0) -> tuple:
    """ Returns a pair:
        - complete git add module lines
        - sub-modules
    """
    assert hashes, "No hashes"
    out = sys.stderr
    exc_these = EXCLUDE_COMPLAIN_ON
    astr = pre
    news, subs = "", ""
    last = ""
    blanked = " " * 3
    with open(fname, "r", encoding="ascii") as fdin:
        line_list = fdin.readlines()
    for aline in line_list:
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
        dock = rest.split(":", maxsplit=1)[-1].split(".git")[0]
        sub = f" {last}" if last else ""
        if rest.startswith("git@github.com:"):
            s_url = f"[{better_path(last)}](https://github.com/{dock})"
        elif dock.startswith("../"):
            s_url = f"[{better_path(last)}](https://www.github.com/serrasqueiro/{dock[len('../'):]})"
        else:
            s_url = f"[{better_path(last)}](https://gist.github.com/serrasqueiro/{dock})"
        if s_url:
            s_url = s_url + f",\n{blanked}+ "
        astring = f"1. {s_url}`" + within + rest + sub + "`\n"
        if debug > 0:
            out.write(
                f"\n\nline: '{line}'\nrest: '{rest}'\ndock: '{dock}'\n"
                f"astring: {astring}\n"
            )
        # If any of specific strings found, do nothing:
        if [item for item in exc_these if item in astring]:
            #print("@@@", astring.replace("\n", "~"))
            astring = ""
        astr += astring
        if rest not in hashes:
            #print(">>>", rest + "!!!\n" + astring, end="<<<\n\n")
            news += astring
        subs += rest + "\n"
        if not out:
            continue
        out.write(f"{line}\n")
    return (news, astr, subs)

def better_path(astr:str) -> str:
    result = astr.replace("_", " ")
    return result

def hashes_there(fname:str="", debug=0):
    assert debug >= 0, "Debug"
    magic_str = "git@gist.github.com:"
    alt_str = "git@github.com:"
    _, _, lines = io_filename(True, fname)
    hashes = []
    last = ""
    for idx, line in enumerate(lines, 1):
        t_flag = magic_str not in line and alt_str not in line
        if debug > 0:
            print(f"::: Line {idx}, t_flag={t_flag}: {line if line else '--'}", end="\n\n" if t_flag else "\n")
        if t_flag:
            last = line
            if debug > 0:
                print(f"::: New hash:", " add ../" in line, line, end="\n\n")
            if " add ../" in line:
                s_hash = line.split(" add ", maxsplit=1)[1].split(" ", maxsplit=1)[0]
                new_hash(s_hash, "N1", hashes)
                #hashes.append(s_hash)
            continue
        pair = line.split(":", maxsplit=1)
        left = pair[0].split(" ")[-1]
        a_hash = pair[1].split(" ")[0]
        assert a_hash, line
        assert last.startswith("1. ["), f"Invalid last: '{last}'"
        sub_dir = last[len("1. ["):].split("]")[0].replace(" ", "_")
        if not os.path.isdir(sub_dir):
            print("#Warn:", "Not a sub dir:", sub_dir)
        s_hash = left + ":" + a_hash
        new_hash(s_hash, "N2", hashes)
        #hashes.append(s_hash)
        last = line
        if debug > 0:
            print(f"::: Line {idx}, s_hash:", s_hash, end="\n\n")
    return hashes

def new_hash(astr, kind, hashes):
    assert astr, "new_hash()"
    assert isinstance(kind, str) and kind, "N1|N2"
    if kind == "N1":
        assert astr.endswith(".git"), astr
    elif kind == "N2":
        assert astr.startswith("git@gist.github.com:"), astr
        assert astr.endswith(".git"), astr
    else:
        return False
    hashes.append(astr)
    if DEBUG > 0:
        print(":::", len(hashes), kind, astr)
    return True

def io_filename(to_read:bool, fname:str=""):
    """ Opens file and returns triplet:
		file-descriptor
		filename
		list of lines
    """
    enc = "ISO-8859-1"
    path = fname if fname else IO_FILE
    if to_read:
        with open(path, "r", encoding=enc) as fdin:
            lines = fdin.read().splitlines()
        return fdin, path, lines
    fdout = open(path, "a", encoding=enc)
    return fdout, path, []

def append_data(news):
    if not news:
        return False
    fdout, _, _ = io_filename(False)
    fdout.write(news)
    fdout.close()
    return True

if __name__=="__main__":
    main()
