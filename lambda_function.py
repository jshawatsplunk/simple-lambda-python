import json

import signalfx_lambda

print('Loading function')
# custom metric example

@signalfx_lambda.emits_metrics() 
def lambda_handler(event, context):
    signalfx_lambda.send_counter('totally.custom.metric.callcount', 12)
    signalfx_lambda.send_gauge('totally.custom.metric.resptime', 110, {'abc':'def'})
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }
