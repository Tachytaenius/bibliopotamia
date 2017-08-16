import markdown2, os

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

data = markdown2.markdown(data, extras=["header-ids, footnotes"])

while(True):
    out = input("Where'd you like your output HTML file? Enter: ")
    if(not os.path.exists(out)):
        break
    if(input("The file already exists. Are you sure you want to overwrite it? (Y or otherwise.) > ").upper() == 'Y'):
        break

with open(out, 'w') as output:
    output.write(data)