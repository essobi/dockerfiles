FROM consul  
  
MAINTAINER Carlos León <mail@carlosleon.info>n  
  
ENV WEBUIDIR=/consul/webui  
  
ADD
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip
/tmp/webui.zip  
  
# Install the consul web ui.  
RUN mkdir -p ${WEBUIDIR} && unzip /tmp/webui.zip -d ${WEBUIDIR}  
  
# Remove temp files  
RUN rm /tmp/webui.zip  
  
ENTRYPOINT ["/bin/consul"]  
  
CMD ["agent", "-data-dir=/consul/data", "-config-dir=/consul/config"]  

