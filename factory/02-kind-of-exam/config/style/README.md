WARNING
-------

Start by using one existing style. Note that you have to keep special comments ``% == ... == %`` where ``...`` is one of the following text :
  * ``PACKAGES USED``
  * ``DEFINITIONS``


TODO
----

You must define two commands and one environment :

  1) ``@build@layout`` builds the main layout.

  2) ``@add@delivery@material`` adds material where the students must give their name.

  3) ``@preamble@style`` is a basic environment just for the style to use with preambles (centering and width are managed before by ``lyxam``).


NOTE
----

  1) The name of your ``sty`` file will be the name of your style.

  2) The following packages are loaded by ``lyxam``.
     i) ``calc``
     ii) ``etoolbox``
     iii) ``fancyhdr``
     iv) ``lastpage``
     v) ``listofitems``
     vi) ``simplekv``
     vii) ``xstring``

  3) The options used are stored in macros ``\@lyxam@<<KEY>>`` where ``<<KEY>>`` is one of the option of the macro ``\exam``. To test if a value is an empty string, you must use ``\@if@empty{\@lyxam@<<KEY>>}{TRUE}{FALSE}``.

  4) One ``etoolbox`` boolean must be managed : ``@lyxam@show@headers@footers`` is to show or hide the headers and footers.

  5) You have the following important translated texts to use for the delivery material :
     i) ``\lyxam@text@name``
     ii) ``\lyxam@text@firstname``

  6) You can also use ``\@lyxam@longduration{#1}`` which gives the text ``"Duration:"``, or its translated version, followed by the value of ``#1``.


GOOD PRACTICE
-------------

For your own commands, use a prefix like ``@nameofmystyle@`` such as to avoid conflict with global commands.
