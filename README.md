# mex

#
# Higher Level Abstraction to re.match() to extract parameters
# Never allow user to specify their own regex, this is the idea of this
# abstraction or simplification - always keep it simple, support a new
# var type if need.
#
# Language
#   var_1;var_2;var_3;..
# where
#   var_x = <var_name>,<var_type>,<expression_1>&<expression_2>&...
#
# <var_name> can be anything but must be unique among the variables
# <var_type> can be
#    - int
#    - float
#    - number (string instead of integer and will not remove leading 0's)
#    - time (12:30:55, 23:59)
#    - email
# <expression_x> is the word you expect to see before/after the parameter
#
