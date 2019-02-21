About this package
==================

**ly-xam**, which is a contraction of **lycée** and **exam**, has been built to facilitate the writings of sheets of exercises and tests.


I beg your pardon for my english...
===================================

English is not my native language, so be nice if you notice misunderstandings, misspellings or grammatical errors in my documents and my codes.


<!--
Incoming new version...
=======================
  -->

Minor changes in this version `1.0.2-beta`
==========================================

**One small bug repaired:** the factory stopped to make PDF examples ! This is has been fixed.



Minor changes in this version `1.0.1-beta`
==========================================

**Change of the name of the option ``theme`` of the macro ``\exam``:** now we have to use ``topic`` which is a better translation.


**Update of the design:** backgrounds no longer have a color because this can cause problem when photocopying exams.



Changes in this version `1.0.0-beta`
====================================

**New package option ``score`` and new macro ``\scpts``:** this allows to add scores or marks when evaluating the tests of students.


**One new option ``pts`` for the macro ``\exam``:** this allows to indicate the total number of points used to evaluate an exam.


**Star versions of exercises.**

1. No star version like ``\exercise`` is for auto-numbered exercises.

2. Simple star version like ``\exercise*`` is for unnumbered exercises.

3. Double star version like ``\exercise**`` is for exercises using a title instead of the standard name.


**Unuseful package options removed:** ``about``, ``hf``, ``noshort``, ``pts`` and ``src`` have been deleted.


Changes in this version `0.3.0-beta`
====================================

**Three new styles.**

1. The style ``mini`` tries to minimize the space used for the formatting. This is the new default style.

2. The style ``book`` has been added to use exercises inside a book or a lesson.

3. The style ``ecolo`` mixes the styles ``mini`` and ``book`` such as to print tests wasting less spaces as possible.


Changes in this version `0.2.0-beta`
====================================

**Three new package options.**

1. ``linebox`` gives a new style for formatting things using frames and lines.

2. ``short`` and ``noshort`` allow to print or not short versions of names of contexts, of time, points...

3. ``about`` and ``noabout`` ask to show or hide infos about topics, exercises and parts.


**New name for the option ``render`` of ``\exam``:** the new name is ``deliver``.


**Two options added to the environment `\begin{preamble}...\end{preamble}`:** one to center or not the content of the premble, and another to define the width of the preamble.


**Customization of the numbers for contexts:** it is now possible to change the way the numbers are printed for each kind of exercises.


Changes in this version `0.1.0-beta`
====================================

**Two new options ``hf`` and ``nohf`` for the pacakage:** this is for showing or hiding the headers and footers.


**Changes for `\exam`.**

1. The option `preamble` has been removed, and all other options are now optional.

2. The macro `\exam` can be used several times in the same document.


**New environment `\begin{preamble}...\end{preamble}`:** you can use it anywhere.


**Changes for macros like `\exercise`:** the option `note` has been renamed `about`.


**Style `APMEP`:** it loads ``\usepackage{fourier-orns}`` instead of ``\usepackage{fourier}`` to only use the ornements. If you still want to have the previous font loaded by `APMEP`, just add ``\usepackage{pxfonts}`` in your preamble.


**Internal changes:** the code has been totally rebuild and simplified thanks to the package `simplekv`.


About this first version `0.0.0-beta`
=====================================

There is only one french documentation `lyxam-doc[fr].pdf` inside the folder `lyxam`.

The only thing needed to use the package is the folder `lyxam` *(you can remove the examples)*.
