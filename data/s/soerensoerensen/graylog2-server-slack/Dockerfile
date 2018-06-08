FROM graylog2/server:2.4.4-1  
LABEL maintainer="https://github.com/soerenschneider/graylog-docker-slack"  
  
ENV PLUGIN_VERSION 3.1.0  
# Use 'ADD --chown=graylog:graylog' in future version:
https://github.com/moby/moby/pull/34263  
ADD https://github.com/graylog-labs/graylog-plugin-
slack/releases/download/${PLUGIN_VERSION}/graylog-plugin-
slack-${PLUGIN_VERSION}.jar /usr/share/graylog/plugin/  
RUN chown graylog:graylog /usr/share/graylog/plugin/graylog-plugin-
slack-${PLUGIN_VERSION}.jar  

