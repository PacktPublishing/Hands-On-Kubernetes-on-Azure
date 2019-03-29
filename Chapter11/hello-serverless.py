# The framework is all setup to take in a 
# user defined handler function (hello in this case)
# and pass data along with the event array
def hello(event, context):
   print event   return event['data']