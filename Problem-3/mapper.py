#!/usr/bin/env python
"""mapper.py"""

import sys
# getting input using sys.stdin
for every_line in sys.stdin:

#stripping every line which we get from input.

	every_line = every_line.strip()
	every_line = every_line.strip("[")
	every_line = every_line.strip("]")
	every_line = every_line.replace("\"","")

#splitting using , and space.

	friend_list = every_line.split(", ", 1)

#prints with a tab space in between.

	print '%s\t%s' % (friend_list[0], 1)
