FROM consul:0.7.3  
LABEL container.name="baffolobill/consul:0.7.3"  
  
ENV CONSUL_VERSION 0.7.3  
  
RUN apk add --no-cache openssl curl \  
&& wget -q -O /tmp/webui.zip
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip
\  
&& mkdir /ui \  
&& cd /ui \  
&& unzip /tmp/webui.zip \  
&& rm /tmp/webui.zip  
#RUN apk update && apk add bash curl tini  
  
#VOLUME ["/config.d"]  
  
#RUN mkdir /config  
  
#ADD ./config/consul.json /config/consul.json  
#ONBUILD ADD ./config /config/  
  
#ADD ./start /bin/start  
  
#EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
#ENTRYPOINT ["tini", "--", "/bin/start"]  
#CMD []  

