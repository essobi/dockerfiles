FROM docker.elastic.co/logstash/logstash:5.5.2  
  
COPY ./ /app/  
  
  
RUN cat /app/ls-plugins | xargs logstash-plugin install  
  
USER root  
  
RUN yum -y install epel-release && \  
yum -y install python-pip vim && \  
yum clean all  
  
RUN pip install hvac  
  
EXPOSE 5001:5001  
  
RUN chown -R logstash /app  
  
USER logstash  
  
# RUN /usr/share/logstash/bin/logstash -t -f /app/logstash-config.conf  
  
ENTRYPOINT "/app/entrypoint.sh"  
CMD ""  

