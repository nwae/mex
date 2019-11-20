# -*- coding: utf-8 -*-

import flask
import nwae.utils.Log as lg
from inspect import currentframe, getframeinfo
import mex.MatchExpression as mx
import json


#
# Flask is not multithreaded, all requests are lined up. This explains why request
# variables are global.
# To make it multithreaded, we declare this app application that already implements
# the method required by the WSGI (gunicorn)
#
app = flask.Flask(__name__)

def Start_Mex_API():
    obj = MexAPI()
    return obj

#
# Flask DOES NOT run in multithreaded mode and handle 1 request at
# one time. Wrap it with gunicorn.
#
class MexAPI:

    EXAMPLE_USAGE = \
        'http://localhost:5000/mex?'\
        +'ret=1&'\
        +'pattern=m,float,dollar/dollars/make/$;y,int,year/yr&'\
        +'txt=my salary in year 2019 is $8888.'

    def __init_rest_urls(self):
        #
        # Mex parameters extraction
        #
        @self.app.route('/mex', methods=['GET'])
        def gbot_api_get_mex_params():
            pattern = self.get_param(param_name='pattern', method='GET')
            text = self.get_param(param_name='txt', method='GET')
            ret_how_many = self.get_param(param_name='ret', method='GET')

            if not (pattern and text):
                return 'Missing parameters "pattern" or "txt". '\
                       + 'Example Usage: "' + MexAPI.EXAMPLE_USAGE + '".'
            ret_one_value = True
            if ret_how_many == '2':
                ret_one_value = False
            return self.get_mex_params(
                pattern=pattern, text=text, return_one_value=ret_one_value
            )
        @self.app.errorhandler(404)
        def page_not_found(e):
            lg.Log.error(str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                       + ': Resource [' + str(flask.request.url) + '] is not valid!')
            return "<h1>404</h1><p>The resource could not be found.</p>", 404

    def __init__(
            self
    ):
        self.app = app
        self.app.config['DEBUG'] = False
        self.__init_rest_urls()
        return

    def get_mex_params(
            self,
            pattern,
            text,
            return_one_value
    ):
        try:
            if return_one_value in (None, ''):
                return_one_value = True
            cmobj = mx.MatchExpression(
                pattern = pattern
            )
            params_all = cmobj.get_params(
                sentence = text,
                return_one_value = return_one_value
            )
            return json.dumps(params_all)
        except Exception as ex:
            errmsg = str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                     + ' Exception occurred get mex params for IP ' + str(flask.request.remote_addr) \
                     + ', pattern "' + str(pattern) + '", text "' + str(text)\
                     + '", exception ' + str(ex) + '.'
            lg.Log.error(errmsg)
            if lg.Log.DEBUG_PRINT_ALL_TO_SCREEN:
                raise Exception(errmsg)
            return errmsg

    def get_param(self, param_name, method='GET'):
        if method == 'GET':
            if param_name in flask.request.args:
                return str(flask.request.args[param_name])
            else:
                return ''
        else:
            try:
                val = flask.request.json[param_name]
                return val
            except Exception as ex:
                lg.Log.critical(str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                           + ': No param name [' + param_name + '] in request.')
                return None

    def run_mex_api(self, host='0.0.0.0'):
        self.app.run(
            host = host,
            port = 5000,
            # threaded = True
        )


if __name__ == '__main__':
    #lg.Log.LOGLEVEL = lg.Log.LOG_LEVEL_DEBUG_2
    #lg.Log.DEBUG_PRINT_ALL_TO_SCREEN = True
    intent_api_instance = Start_Mex_API()
    intent_api_instance.run_mex_api()
