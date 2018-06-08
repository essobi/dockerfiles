FROM fluent/fluentd:v0.12.26  
USER root  
  
ADD ./scripts /etc/fluentd-scripts  
ADD ./fluentd.conf /etc/fluentd-conf/fluentd.conf  
ADD ./logentries-plugin.rb /etc/fluentd-plugins/logentries-plugin.rb  
  
RUN apk add --update bash && rm -rf /var/cache/apk/* \  
&& chmod +x /etc/fluentd-scripts/*.sh  
  
CMD /etc/fluentd-scripts/start-agent.sh  

