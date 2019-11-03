# mex

Human Level Description of extracting parameters from sentence WITHOUT
technical regular expression syntax.

Higher Level Abstraction to re.match() to extract parameters
Never allow user to specify their own regex, this is the idea of this
abstraction or simplification - always keep it simple, support a new
var type if need.

Language
  var_1;var_2;var_3;..
where
  var_x = <var_name>,<var_type>,<expression_1>&<expression_2>&...
In human level, the above says,
  "Please extract variable x using <var_name> (e.g. email, date,
  and this variable is of type <var_type> (e.g. float, email, time")
  and expect a person to type words "<expression_1>" or "<expression_2>"...
  when presenting this parameter"

<var_name> can be anything but must be unique among the variables
<var_type> can be
   - int
   - float
   - number (string instead of integer and will not remove leading 0's)
   - time (12:30:55, 23:59)
   - datetime (20190322 23:59:11, 2019-03-22 23:59, 2019-03-22)
   - email
<expression_x> is the word you expect to see before/after the parameter

