#!/usr/bin/env python

from modules import socketio, app, cbpi
import pydevd_pycharm
import os

if 'DEBUG_SERVER' in os.environ:
  pydevd_pycharm.settrace(os.environ['DEBUG_SERVER'], port=58881, stdoutToServer=True, stderrToServer=True)

try:
  port = int(cbpi.get_config_parameter('port', '5000'))
except ValueError:
  port = 5000

socketio.run(app, host='0.0.0.0', port=port)

