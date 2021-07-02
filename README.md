# simple-lambda-python
Super simple lambda function in python that shows sending custom metrics using signalfx-python library

1. Create an AWS lambda function for python 3.8 runtime. https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html
2. Copy the sample code into your lambda_handler (uses the signalfx_lambda module).
4. Add the signalfx lambda wrapper as a layer by specifying the ARN that can be found here: https://github.com/signalfx/lambda-layer-versions/blob/master/python/PYTHON.md.
5. Add your environment variable(s) (env.txt) under Configuration. If sending metrics to a collector, just the metrics endpoint is needed. If sending directly to signalfx.com ingest endpoint, then also add your access token. 
6. Create a test event with some basic inputs for your test. (test.json)
7. Test it.
8. Search Splunk Observability Cloud for your custom metrics using Metric Finder or creating a chart and browsing for your custom metrics.

![Screenshot](https://github.com/jshawatsplunk/simple-lambda-python/blob/main/custom_metrics_in_MetricFinder.png)
