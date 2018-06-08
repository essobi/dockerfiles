FROM ubuntu  
MAINTAINER Mike Splain msplain@paypal.com  
  
RUN apt-get update && \  
apt-get install curl screen wget unzip -qy  
  
ADD https://dl.bintray.com/mitchellh/consul/0.3.1_linux_amd64.zip
/tmp/consul.zip  
RUN cd /usr/local/sbin && \  
unzip /tmp/consul.zip  
  
ADD https://dl.bintray.com/mitchellh/consul/0.3.1_web_ui.zip
/tmp/consulwebui.zip  
RUN mkdir -p /etc/consulwebui && \  
cd /etc/consulwebui && \  
unzip /tmp/consulwebui.zip  
  
CMD /usr/local/sbin/consul agent -bootstrap -server -ui-dir
/etc/consulwebui/dist -data-dir=/tmp/consul -client=0.0.0.0  
EXPOSE 8400 8500 8600/udp  

