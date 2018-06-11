FROM wickedmonkey/consul-server-bare  
MAINTAINER Robert Landers <landers.robert@gmail.com>  
  
ENV CONSUL_VERSION=0.5.0  
# Download and install Consul-ui  
ADD https://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_web_ui.zip
/tmp/consul_web_ui.zip  
RUN cd /tmp && \  
unzip consul_web_ui.zip && \  
mkdir /ui && \  
mv dist/* /ui && \  
rm consul_web_ui.zip  
  
# Add the files  
ADD root /  
  
# Expose the web ui port  
EXPOSE 8500  

