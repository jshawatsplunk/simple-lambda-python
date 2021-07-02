# simple-lambda-python
Super simple lambda function in python that shows sending custom metrics using signalfx-python library

1. Create a lambda function for python 3.8 runtime.
2. Copy the sample code into your lambda_hander that uses the signalfx_lambda module.
4. Add the signalfx lambda wrapper as a layer by specifying the ARN that can be found here: https://github.com/signalfx/lambda-layer-versions/blob/master/python/PYTHON.md.
5. Add your environment variable(s) (example in env.txt). If sending metrics to a collector, just the metrics endpoint is needed. If sending directly to signalfx.com ingest endpoint, then also add your access token. 
6. Create a test event with some basic inputs for your test. (test.json)
7. Test it.
