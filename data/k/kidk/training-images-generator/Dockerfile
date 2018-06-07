FROM python:2-onbuild  
  
MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>  
  
ENV PYTHONUNBUFFERED 0  
  
ENV WEB_HOST web  
ENV RECEIVER_HOST receiver  
  
CMD [ "python", "./main.py" ]  
  
LABEL
com.coscale.monitoring='[{"PluginType":"LOGPLUGIN","Configuration":{"MATCH":["\"/var/log/generator.log\"
\"HISTOGRAM(responseSize)\" \"Generator latency\" \"%{NUMBER:responseSize}\"
\"ns\""]}}]'  

