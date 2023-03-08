import boto3
import json
import os
import time

ACK_STATE_MACHINE_ARN = os.getenv('ACK_STATE_MACHINE_ARN')
RESPONSE_STATE_MACHINE_ARN = os.getenv('RESPONSE_STATE_MACHINE_ARN')

client = boto3.client('stepfunctions')
def lambda_handler(event, context):
    print(f'Received event {event}')
    payload = event['Records'][0]['body']
    # time.sleep(0.1) # simulating the event processing

    # send the ack event
    ack_response = client.start_execution(
        stateMachineArn=ACK_STATE_MACHINE_ARN,
        # name='string',
        # input=json.dumps(payload)
        input=payload
    )

    time.sleep(0.1) # simulating the event response delay

    # send the response event
    ack_response = client.start_execution(
        stateMachineArn=RESPONSE_STATE_MACHINE_ARN,
        # name='string',
        # input=json.dumps(payload)
        input=payload
    )

    return
