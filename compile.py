# Bibliopotamia (writing workflow.)
# Copyright (C) 2017 Henry "wolfboyft" Fleminger Thomson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import markdown2, os, sys

# Apparently if a python script changes the working directory and terminates, the command prompt will stay at the same directory of invokation, making this whole "backup and restore" system useless.
# wd = os.getcwd() # Make a backup of the user's working directory, because it'll change unless the user runs this script from its superdirectory.

os.chdir(sys.path[0] + "/..")

with open("chapters.txt", 'r') as chapters:
	targets = chapters.read().splitlines()

data = ""

while(True):
	if(not len(targets)):
		if(len(data)):
			# It's unlikely that we won't reach this block, but even so, why attempt to destroy what might not be there?
			data = data.rstrip("\n\n---\n\n") # They say it's easier to ask for forgiveness than permission.
		break
	with open(targets[0], 'r') as chapter:
		data = data + chapter.read().rstrip("\n") + "\n\n---\n\n" # This program hasn't been written in a "look before you leap" approach, so the inevitable "\n\n---\n\n" at the end of the data variable (provided that chapters.txt gave us any chapters (because of how this program was written)) is removed rather than never being added.
	del targets[0]

data = markdown2.markdown(data, extras=["header-ids", "footnotes"])

while(True):
  out = input("Where'd you like your output HTML file, relative to \"" + os.getcwd() + "\"? Enter: ")
  if(not os.path.exists(out)):
    break
  if(input("The file already exists. Are you sure you want to overwrite it? (Y or otherwise.) > ").upper() == 'Y'):
    break

with open(out, 'w') as output:
  output.write(data)

# The following line of code was part of the redundant "backup and restore" system.
# os.chdir(wd) # Now when python closes the user will be where they invoked the script, not the directory above the script which is what the script uses.