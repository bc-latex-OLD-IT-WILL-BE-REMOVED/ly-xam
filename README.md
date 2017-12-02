What about this package  ?
==========================

**ly-xam**, which is a contraction of **lycée** and **exam**, has been built to facilitate the writings of sheets of exercises and tests.


Changes in this version `0.3.0-beta`
====================================

**Three new styles.**

  1) The style ``mini`` tries to minimize the space used for the formatting. This is the new default style.

  2) The style ``book`` has been added to use exercises inside a book or a lesson.

  3) The style ``ecolo`` mixes the styles ``mini`` and ``book`` such as to print tests wasting less spaces as possible.


Changes in this version `0.2.0-beta`
====================================

**Three new package options.**

  1) ``linebox`` gives a new style for formatting things using frames and lines.

  2) ``short`` and ``noshort`` allow to print or not short versions of names of contexts, of time, points...

  3) ``about`` and ``noabout`` ask to show or hide infos about topics, exercises and parts.


**New name for the option ``render`` of ``\exam``:** the new name is ``deliver``.


**Two options added to the environment `\begin{preamble}...\end{preamble}`:** one to center or not the content of the premble, and another to define the width of the preamble.


**Customization of the numbers for contexts:** it is now possible to change the way the numbers are printed for each kind of exercises.


Changes in this version `0.1.0-beta`
====================================

**Two new options ``hf`` and ``nohf`` for the pacakage:** this is for showing or hiding the headers and footers.


**Changes for `\exam`.**

  1) The option `preamble` has been removed, and all other options are now optional.

  2) The macro `\exam` can be used several times in the same document.


**New environment `\begin{preamble}...\end{preamble}`:** you can use it anywhere.


**Changes for macros like `\exercise`:** the option `note` has been renamed `about`.


**Style `APMEP`:** it loads ``\usepackage{fourier-orns}`` instead of ``\usepackage{fourier}`` to only use the ornements. If you still want to have the previous font loaded by `APMEP`, just add ``\usepackage{pxfonts}`` in your preamble.


**Internal changes:** the code has been totally rebuild and simplified thanks to the package `simplekv`.


About this first version `0.0.0-beta`
=====================================

For the moment, there is only one french documentation `lyxam-doc[fr].pdf` inside the folder `lyxam`.

The only thing needed to use the package is the folder `lyxam`.


I beg your pardon for my english...
===================================

English is not my native language, so be nice if you notice misunderstandings, misspellings or grammatical errors in my documents and my codes.