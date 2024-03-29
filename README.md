# Mex (Match EXpression)

Human Level Description of extracting parameters from sentence without
regular expression syntax.

Higher Level Abstraction to ```re.match()``` to extract parameters.

Never allow user to specify their own regex, this is the idea of mex
abstraction or simplification - always keep it simple, support a new
var type if needed.

### Installation

```pip install mex```

### Deployment (Mex Rest API port 5000)

Ready scripts to deploy on any Linux server. Default will run using 3
gunicorn workers using worker type "sync". Configurable in the scripts.
Logs directed to mex/logs/ folder.

```
cd deploy.scripts
./deploy.sh cf=local
```

### Programming Syntax

```
  # For variable 'm' of type float, we look for words 'mass', '무게', 'вес' or '重'
  # For variable 'd' of type datetime, we don't look for any words, just the
  #  datetime string anywhere in the sentence "My mass is 68.5kg on 2019-09-08"
  mex_pat = MatchExpression(
     pattern = 'm, float, mass / 무게 / вес / 重  ;  d, datetime, ',
     lang    = None  # can also be specific 'zh-cn', 'ko', 'th', 'vi', 'en'
  )
  params_dict = mex_pat.get_params(
     sentence         = 'My mass is 68.5kg on 2019-09-08',
     return_one_value = True     # if False will return both (left,right) values
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
```map_vartype_to_regex``` in the constructor.


### Mex Language
```
  var_1  ;  var_2  ;  var_3  ..  var_n  ;  ..
```
where
```
  var_x = <var_name>,  <var_type>,  <expr_1> / <expr_2>/...  , [<len-range>], [<prfdir>]
```
In human level, the above says,

  "Find variable ```x``` using ```<var_name>``` and ```x``` is of data
  type ```<var_type>``` (e.g. float, email, time).
  Expect a person to type words ```<expr_1>``` or ```<expr_2>```...
  when describing this parameter.
  Also it is most likely you will find ```x``` on the ```<prfdir>```
  (left or right) side of the expressions."

```<var_name>```
  can be anything but must be unique among the variables

```<var_type>```
  can be
   - int
   - float (78.99, 1,600.55, 33,000, etc.)
   - number (string instead of integer and will not remove leading 0's)
   - account_numer (same as "number" type, but allow '-')
   - time (12:30:55, 23:59)
   - datetime (20190322 23:59:11, 2019-03-22 23:59, 2019-03-22)
   - username
   - username_nonword (include characters and number/punctuations)
   - email
   - uri
   - any (most accepted characters, but not space)
   - str (any of the languages below, no space)
   - str-en (any Latin string, no space)
   - str-zh-cn (any simplified Chinese string, no space)
   - str-ko (any Hangul string, no space)
   - str-th (any Thai string, no space)
   - str-vi (any Vietnamese string, no space)
   
```<expr_x>```
  is the word you expect to see before/after the parameter.
  If using the special keywords "/" or "&" in the expressions,
  you need to escape them "\\/", "\\&".

```<len_range>```
  is the length range of the variable. e.g. If "2-5", means if anything
  less than length 2, will return None, and if anything longer than 5, will
  be truncated to length 5. If entered as "3", means a strict length 3 where
  smaller lengths return None, longer than 3 returns truncated to 3-length.
  This option has no effect on non-string types like "int", "float".

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


### Future Pipeline

  1. Integrate nwae library with intent detection for common intents (confirmation, negation, order/booking types, etc.)
     This will enable us to return not just param variables, but also the intent class. 
  2. Support for more types like "username", NEs, term abstraction (e.g. action), other language strings, etc.
  3. Support for complex sentences, e. g. "The movie rating, according to AGB was 10.5%."
  4. Optimize speed.


