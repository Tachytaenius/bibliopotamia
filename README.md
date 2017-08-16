# What is this?

Bibliopotamia (approximately Greek for "book river" or "document stream") is a workflow setup that uses python and markdown to allow for separate *.md chapters and a simple way to combine them. Down with nonfree editors with their bloated formats that force others to use said editors! Rise, whichever text editor you wish to use! And if you want your markdown documents to come out in HTML... then _rise, Bibliopotamia!!_

# How does it work?

Individual markdown chapters are linked and ordered by the user in the file "../chapters.txt," ((bibliopotamia is meant to be added to book setups as a submodule, which is a subdirectory. So the work itself will be in bibliopotamia's superdirectory) it's just writing the name of the chapters's file, adding a new line and repeating. Having a trailing newline is safe if you're into that) then a script called "compile.py" is executed. The script concatenates each chapter as directed by the chapters list, separating them using some newlines with a horizontal rule. The resulting string is then converted by markdown2 into an output HTML file, which is then saved where the user wishes (overwite prompt included!)

# How do I use it?
Write your *.md files, one for each chapter to be separated by a horizontal rule. Set your working directory to bibliopotamia, which should be a subdirectory to where your *.md files are. Run compile.py with python, and tell the program where you want to output your HTML file.

As for chapters.txt, remember that it goes in the directory above compile.py (because this is meant to be added as a submodule or just a subdirectory if you're not using git,) along with the chapter files themselves.
00_Title.md will be concatenated with 01_InTheBeginning.md, which will be concatenated to 02_HappilyEverAfter.md, with a horizontal rule between each.
```
00_Title.md
01_InTheBeginning.md
02_HappilyEverAfter.md
```