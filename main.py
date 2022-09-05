from time import sleep as s

# by github/whyisthesheep
## uninterestingusername#0496
titleb = """
    ____                 __                               __
   / __ \___  ____ _____/ /___ ___  ___    ____ ___  ____/ /
  / /_/ / _ \/ __ `/ __  / __ `__ \/ _ \  / __ `__ \/ __  /
 / _, _/  __/ /_/ / /_/ / / / / / /  __/ / / / / / / /_/ /
/_/ |_|\___/\__,_/\__,_/_/ /_/ /_/\___(_)_/ /_/ /_/\__,_/
"""
print(titleb)
print("Helper")
s(2)
print("")
title = input("Input your title: ")
s(0.5)
description = input("Description: ")
print("Please separate the requirements with commas and spaces like this: colorama, time, requests")
reqs = ", " + input("Requirements: ")
reqs = "`" + reqs.replace(",", "\n")
reqs = reqs.replace(" ", "pip install ") + "`"
final = "# " + title + "\n" + "### " + description + "\n" + "## Installation\n" + reqs
print(final)
