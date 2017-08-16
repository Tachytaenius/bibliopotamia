# What is this?

Bibliopotamia (approximately Greek for "book river" or "document stream") is a workflow setup that uses python and markdown to allow for separate *.md chapters and a simple way to combine them. Down with nonfree editors with their bloated formats that force others to use said editors! Rise, whichever text editor you wish to use! And if you want your markdown documents to come out in HTML... then _rise, Bibliopotamia!!_

# How does it work?

Individual markdown chapters are linked and ordered by the user in a file called "chapters.txt," (it's just writing the name of the chapters's file, adding a new line and repeating. Having a trailing newline is safe if you're into that) then a script called "compile.py" is ran (or an executable form of such a script.) The script concatenates each chapter as directed by the chapters list, separating them using some newlines with a horizontal rule. The resulting string is then converted by markdown2 into an output HTML file, which is then saved where the user wishes (overwite prompt included!)

# I'd like to use this, but I need an example of a chapters file.

Remember that chapters.txt goes where compile.py and the chapter files themselves do.
00_Title.md will be concatenated with 01_InTheBeginning.md, which will be concatenated to 02_HappilyEverAfter.md, separating each with a horizontal rule.
```
00_Title.md
01_InTheBeginning.md
02_HappilyEverAfter.md
```