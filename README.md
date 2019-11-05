# mex (Match EXpression)

Human Level Description of extracting parameters from sentence WITHOUT
ugly and technical overkill of regular expression syntax.

Higher Level Abstraction to ```re.match()``` to extract parameters.

NEVER allow user to specify their own regex, this is the idea of mex
abstraction or simplification - always keep it simple, support a new
var type if needed.


### Programming Syntax

```
  # For variable 'm' of type float, we look for words 'mass', 'вес' or '重'
  # For variable 'd' of type datetime, we don't look for any words, just the
  #  datetime string anywhere in the sentence "My mass is 68.5kg on 2019-09-08"
  mex_pat = MatchExpression(
     pattern = 'm, float, mass / вес / 重  ;  d, datetime, ',
  )
  params_dict = mex_pat.get_params(
     sentence = 'My mass is 68.5kg on 2019-09-08',
     return_one_value = True
  )
```

will return a Python dictionary type,

```
  params_dict = {"m": 68.5, "d": "2019-09-08"}
```

If ```return_one_value = False```, return value is

```
  # mass found on the right side, and date on the left
  params_dict = {"m": [null, 68.5], "d": ["2019-09-08", null]}
```

For customization of your own data types, you may utilize the parameter
"map_vartype_to_regex" in the constructor.


### Language
```
  var_1;var_2;var_3;..
```
where
```
  var_x = <var_name>,  <var_type>,  <expr_1> / <expr_2>/...  , [<prfdir>]
```
In human level, the above says,

  "Please extract variable x using <var_name> and this variable is of
  type <var_type> (e.g. float, email, time).
  Expect a person to type words "<expr_1>" or "<expr_2>"... when describing
  this parameter".
  "<prfdir>" is the preferred direction of the parameter to extract when
  specified to return only 1 value. This parameter is optional

```<var_name>```
  can be anything but must be unique among the variables

```<var_type>```
  can be
   - int
   - float
   - number (string instead of integer and will not remove leading 0's)
   - time (12:30:55, 23:59)
   - datetime (20190322 23:59:11, 2019-03-22 23:59, 2019-03-22)
   - email
   - str-en (any Latin string)
   - str-zh-cn (any simplified Chinese string)
   - str-ko (any Hangul string)
   - str-th (any Thai string)
   - str-vi (any Vietnamese string)
   
```<expr_x>```
  is the word you expect to see before/after the parameter

```<prfdir>```
  is the preferred direction if ```return_one_value == True```, otherwise it
  has no effect.
  This parameter is optional, and most of the time is left out since we
  can already return both left/right values for the user to choose.


### Built-in Algorithm

  - Proper sorting of longest to shortest of expressions to ensure
    correctness of results
  - Right side matching ignored when no expressions given
  - Built-in types with stable regex


### TODOs

  1. 