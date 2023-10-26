# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Función que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
import traceback

base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'Cloudwatch', 'libs')

if cur_path not in sys.path:
    sys.path.append(cur_path)

import boto3
from LogsObject import LogsObject
global mod_cloudwatch_session

try:
    if not mod_cloudwatch_session:
        mod_cloudwatch_session = None
except NameError:
    mod_cloudwatch_session = None


"""
    Functions
"""
def parse_rocketbot_logs(file_path):
    from datetime import datetime, timezone

    log_events = []

    with open(file_path, 'r') as log_file:
        for line in log_file:
            parts = line.split(' - ')

            if len(parts) >= 2:
                timestamp_str = parts[0].strip()
                message = '-'.join(parts[1:]).strip()

                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
                epoch_time = int(timestamp.timestamp() * 1000)

                log_events.append({
                    'timestamp': epoch_time,
                    'message': message
                })

    return log_events





"""
    Get the module that was invoked
"""
module = GetParams("module")

try:
    if module == "connect":
        awsAccessKeyId = GetParams("access_id")
        awsSecretAccessKey = GetParams("secret_key")
        region = GetParams("region") or "us-east-1"
        result = GetParams('result')

        try:
            mod_cloudwatch_session = LogsObject(awsAccessKeyId, awsSecretAccessKey, region)
            # The method is called to know if the connection is established or not
            mod_cloudwatch_session.getAccountPolicies()
            
            if result:
                SetVar(result, True)

        except Exception as e:
            mod_cloudwatch_session = None
            if result:
                SetVar(result, False)
            raise e

    else:
        if not mod_cloudwatch_session:
            raise Exception("You must connect to AWS first")

    if module == "create_log_group":
        name = GetParams("name")
        result = GetParams('result')

        try:
            response = mod_cloudwatch_session.createLogGroup(name)
            print(response)

            if result:
                SetVar(result, True)

        except Exception as e:
            if result:
                SetVar(result, False)
            raise e

    if module == "delete_log_group":
        name = GetParams("name")
        result = GetParams('result')

        try:
            response = mod_cloudwatch_session.deleteLogGroup(name)
            print(response)

            if result:
                SetVar(result, True)

        except Exception as e:
            if result:
                SetVar(result, False)
            raise e

    if module == "create_log_stream":
        logGroupName = GetParams("log_group_name")
        logStreamName = GetParams("log_stream_name")
        result = GetParams('result')

        try:
            response = mod_cloudwatch_session.createLogStream(logGroupName, logStreamName)
            print(response)

            if result:
                SetVar(result, True)

        except Exception as e:
            if result:
                SetVar(result, False)
            raise e

    if module == "delete_log_stream":
        logGroupName = GetParams("log_group_name")
        logStreamName = GetParams("log_stream_name")
        result = GetParams('result')

        try:
            response = mod_cloudwatch_session.deleteLogStream(logGroupName, logStreamName)
            print(response)

            if result:
                SetVar(result, True)

        except Exception as e:
            if result:
                SetVar(result, False)
            raise e

    if module == "put_log_events":
        logGroupName = GetParams("log_group_name")
        logStreamName = GetParams("log_stream_name")
        logEvents = GetParams("log_events")
        rocketbot_log = GetParams("rocketbot_log")
        result = GetParams('result')

        try:
            
            if rocketbot_log:
                logEvents = parse_rocketbot_logs(rocketbot_log)
            else:
                logEvents = eval(logEvents)
            response = mod_cloudwatch_session.putLogEvents(logGroupName, logStreamName, logEvents)

            if result:
                SetVar(result, True)

        except Exception as e:
            if result:
                SetVar(result, False)
            raise e

    if module == "get_log_events":
        logGroupName = GetParams("log_group_name")
        logStreamName = GetParams("log_stream_name")
        result = GetParams('result')

        try:
            response = mod_cloudwatch_session.getLogEvents(logGroupName, logStreamName)
            print(response)

            if result:
                SetVar(result, response.get('events', []))

        except Exception as e:
            if result:
                SetVar(result, False)
            raise e

    if module == "filter_log_events":
        logGroupName = GetParams("log_group_name")
        logStreamName = GetParams("log_stream_name")
        filterPattern = GetParams("filter_pattern")
        result = GetParams('result')

        try:
            response = mod_cloudwatch_session.filterLogEvents(logGroupName, logStreamName, filterPattern)
            print(response)

            if result:
                SetVar(result, response.get('events', []))

        except Exception as e:
            if result:
                SetVar(result, False)
            raise e

except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e
