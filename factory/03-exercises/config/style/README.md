WARNING
-------

Start by using one existing style. Note that you have to keep special comments ``% == ... == %`` where ``...`` is one of the following text :
  * ``PACKAGES USED``
  * ``DEFINITIONS``


TODO
----

You must define on single command ``\@build@ctxt`` whith two arguments.

  1) Argument ``#1`` is the kind of context: ``topic``, ``exercise``...

  2) Argument ``#2`` is either ``hidectxt`` or ``showctxt`` so has to show or hide the text for the context. Just use ``\IfStrEq{#2}{hidectxt}{HIDE}{SHOW}`` in your code.


NOTE
----

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

  3) The options used are stored in macros ``\@lyxam@ctxt@<<KEY>>`` where ``<<KEY>>`` is one of the option. To test if a value is an empty string, you must use ``\@if@empty{\@lyxam@<<KEY>>}{TRUE}{FALSE}``.

  4) To print the name, shorten or not, of the context, just use ``\@lyxam@ctxt@name{<<CTX>>}`` where ``<<CTX>>`` is the name of the context.
  You can also use ``\@lyxam@if@end@with@colon{<<CTX>>}{TRUE}{FALSE}`` if you need to know that the name of the context finishes by a colon (thinks of case like "Ex.1").

  5) To print the number of the context, just use one time ``\@lyxam@ctxt@nb{<<CTX>>}`` where ``<<CTX>>`` is the name of the context.

  6) You can also use the following command where ``<<CTX>>`` is the name of the context.

     i) ``\@lyxam@ctxt@longpoints{<<CTX>>}`` gives either nothing, or ``"No point"``, or ``"1 point"`` or ``"X points"``.

     ii) ``\@lyxam@ctxt@longsource{<<CTX>>}`` gives either nothing, or ``"Source:..."``.

     iii) ``\@lyxam@ctxt@longtime{<<CTX>>}`` gives either nothing, or ```"Time:..."```.


GOOD PRACTICE
-------------

For your own commands, use a prefix like ``@nameofmystyle@`` such as to avoid conflict with global commands.
