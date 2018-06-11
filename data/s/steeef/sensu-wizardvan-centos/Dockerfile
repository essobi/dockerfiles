FROM steeef/sensu-centos  
MAINTAINER Stephen Price <steeef@gmail.com>  
  
RUN yum -y install git  
  
RUN git clone https://github.com/opower/sensu-metrics-relay.git /tmp/wizardvan  
RUN cp -R /tmp/wizardvan/lib/sensu/extensions/* /etc/sensu/extensions/  
RUN rm -rf /tmp/wizardvan  
  
EXPOSE 15672  
EXPOSE 8080  
EXPOSE 22  
ADD start.sh /tmp/start.sh  
RUN chmod +x /tmp/start.sh  
CMD /tmp/start.sh  

