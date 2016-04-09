# Dissy usage #
Open an ELF file from Dissy. It currently needs to be non-stripped.

  * Dissy shows jumps with red links to the destination address
  * A label is used to show call destinations
  * Clicking or pressing enter on calls or jumps will take you to the destination function / address
  * Dissy supports interactive searching for labels and addresses both for functions and instructions. Just start typing.
  * The lookup (use **Ctrl-l** to access) feature allows for looking up pasted addresses or labels. The lookup is intelligent in that it tries to convert common patterns into numbers before reverting to label lookup.
  * Multiple words/addresses in the lookup bar is allowed (and will add a "callchain" to the history)
  * A text entry box for highlighting patterns (use **Ctrl-k** to access) for example to display all accesses to a group of registers
  * History navigation like in web browsers (returning to the last function, **Alt-Left** and **Alt-Right**)

# Bugs #
Report bugs in the issue tracker. Questions and comments can also be sent to [simon.kagstrom@gmail.com](mailto:simon.kagstrom@gmail.com)