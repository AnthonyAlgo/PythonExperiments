def lambda_handler(event, context):
  #do something with the event data
  event_data = event['payload']
  #store the payload
  return event_data