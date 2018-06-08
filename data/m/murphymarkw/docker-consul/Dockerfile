FROM busybox  
MAINTAINER Mark Murphy <murphy.mark.w+github@gmail.com>  
  
ADD https://releases.hashicorp.com/consul/0.6.0/consul_0.6.0_linux_amd64.zip
/tmp/consul.zip  
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm
/tmp/consul.zip  
  
ADD https://releases.hashicorp.com/consul/0.6.0/consul_0.6.0_web_ui.zip
/tmp/webui.zip  
RUN cd /tmp && unzip /tmp/webui.zip && mv static /ui && rm /tmp/webui.zip  
  
EXPOSE 8300  
EXPOSE 8301 8301/udp  
EXPOSE 8302 8302/udp  
EXPOSE 8400  
EXPOSE 8500  
EXPOSE 53/udp  
  
ENTRYPOINT ["/bin/consul"]  

