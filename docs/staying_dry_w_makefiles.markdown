---
layout: presentation
title: Makefile-presentation
permalink: /Makefile-presentation/
---

# Staying D.R.Y. with Makefiles

---

# You don't want to be W.E.T.

* Waiting (for unnecessary reprocessing)
* Editing (manual temporary edits of scripts)
* Time-wasting (easy parallel processing)

---

# Makefiles - they're for compiling C/C++, right?

Yes, and ...
1. Anything you'd normally use a shell script to do
2. Easy parallel-processing
3. Keeping track of dependencies so you don't have to keep them in mind

---

# What are they? 

* _make_ is the executable, a _Makefile_ is the script

* Makefiles are text files with a particular syntax

```make
# comment
target: prerequisite(s)
	recipe # NOTE: tab-prefixed line
```

```make
pizza: dough sauce cheese
	shape dough
	spread sauce
	sprinkle cheese
	bake > pizza
```


```make
.PHONY: default clean

default: file.txt.gz

file.txt.gz: raw_data.txt
	cat raw_data.txt|sed '1d' |gzip -c - > file.txt

clean:
	rm file.txt.gz
```
---

# How to use Makefiles

* _make_ is the executable that interprets a Makefile
* How make "thinks"
   * Parsing the file
      * Default Rule
      * 2 Phases
         1. Internalize variables/values and create a dependency graph (the plan)
         1. Determine which targets need to be updated (based on last-modified-time aka timestamp), and run the recipes needed to update them

   * Executing the plan
      * Each line of a recipe is run in a separate sub-shell
         * /bin/sh by default
         * unless you use .ONESHELL, which comes with other caveats/behavior changes
      * Make stops if any step in a recipe has a non-zero return code
        * Unless you use `-command` in the recipe or `-i` on the cmd line

---
# Dependency Graph (a.k.a DAG)
test
test2
![image]({{ site.baseurl }}/assets/images/diagram.svg)
---

# How to use Makefiles
## _Always_ do a dry run - find out what make will run first
```bash
# make the default target, as a dry run
make -n
# OR
# make a specific target, as a dry run
make -n my_target
```

## Run make, and if you can, run steps in parallel
```bash
# Run make serially, for the default target
make
# OR
# Run make with 8 job slots (subprocesses)
make -j8
```

---

# How to use Makefiles
## Common errors/issues and solutions
* `make: *** No rule to make target 'blah'.  Stop.` 
  * _Make doesn't know how to build this file_
  * You could have a misspelled target in the Makefile, or you are specifying a target on the cmd line that's not defined in the Makefile

* Your makefile always wants to build file, even when it's up to date
  * Make uses timestamps to tell when a file is out of date.  If the timestamp of the file wasn't updated, or was updated too quickly, you may need to add the following as a last step to the recipe
```makefile
	sleep 1; touch -c $@ # waitasecond, then update the timestamp
```
* Your recipe doesn't create a file on the available filesystem (i.e. it updates a db or makes a rest call)
  * Create a log file and use that as the target of the recipe
  * Consider using `command | tee logfile.log`

---

# Shortcuts: how to not repeat yourself in Makefile code

* Use Variables (immediate vs. deferred)
* Use Default targets, prerequisites
  * $@ - the recipe target
  * $^ - all prerequisites of the recipe
  * $< - the first prerequisite of the recipe

```make
output.txt : file1.txt file2.txt
	cat file1.txt file2.txt > output_file.txt

# YOU CAN REWRITE THE ABOVE AS ...
output.txt : file1.txt file2.txt
	cat $^ > $@
```
* Use `$(shell cmd)` to run capture the output of shell commands as a make var

```make
CSV_FILES:= $(shell ls *.csv)
```

---

# The Situation where Makefiles will _really_ save you time
* the "I haven't looked at this code in a year" scenario
  * and now there's a bug ...

* By clearly specifying the targets and prerequisites, you don't have to have the project steps and dependencies in your brain
* Re-running parts of projects, responding to bugs/changes becomes trivial

---

# Scenario

---

# Recap
## Stay D.R.Y.
## Save Time
## Use Make
