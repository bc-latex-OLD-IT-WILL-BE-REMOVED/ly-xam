What about this package  ?
==========================

**ly-xam**, which is a contraction of **lycée** and **exam**, has been built to facilitate the writings of sheets of exercises and tests.


Changes in the next incoming version...
=======================================

**New name for the option ``render`` of ``\exam``:** the new name is ``deliver``.


**New package option ``short`` and ``noshort``:** this is to print or not short versions of names of contexts.


**Customization of numbers for contexts:** it is now possible and easy to choose the kind of numbers printed for the contexts.



**[to be continued...]**


Changes in this version `0.1.0-beta`
====================================

**Two new options ``hf`` and ``nohf`` for the pacakage:** this is for showing or hiding the headers and footers.


**Changes for `\exam`.**

  1) The option `preambule` has been removed, and all other options are now optional.

  2) The macro `\exam` can be used several times in the same document.


**New environment `\begin{preambule}...\end{preambule}`:** you can use it anywhere.


**Changes for macros like `\exercise`:** the option `note` has been renamed `about`.


**Style `APMEP`:** it loads ``\usepackage{fourier-orns}`` instead of ``\usepackage{fourier}`` to only use the ornements. If you still want to have the previous font loaded by `APMEP`, just add ``\usepackage{pxfonts}`` in your preambule.


**Internal changes:** the code has been totally rebuild and simplified thanks to the package `simplekv`.


About this first version `0.0.0-beta`
=====================================

For the moment, there is only one french documentation `lyxam-doc[fr].pdf` inside the folder `lyxam`.

The only thing needed to use the package is the folder `lyxam`.


I beg your pardon for my english...
===================================

English is not my native language, so be nice if you notice misunderstandings, misspellings or grammatical errors in my documents and my codes.