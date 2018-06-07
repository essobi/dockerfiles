FROM graylog2/server:2.4.3-1  
ENV SLACK_PLUGIN_VERSION 3.0.1  
RUN set -x \  
&& wget -O /usr/share/graylog/plugin/graylog-plugin-
slack-${SLACK_PLUGIN_VERSION}.jar https://github.com/graylog-labs/graylog-
plugin-slack/releases/download/${SLACK_PLUGIN_VERSION}/graylog-plugin-
slack-${SLACK_PLUGIN_VERSION}.jar  

