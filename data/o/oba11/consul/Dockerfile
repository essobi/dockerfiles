FROM progrium/busybox  
  
ENV CONSUL_VER 0.5.0  
ADD https://dl.bintray.com/mitchellh/consul/${CONSUL_VER}_linux_amd64.zip
/tmp/consul.zip  
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm
/tmp/consul.zip  
  
ADD https://dl.bintray.com/mitchellh/consul/${CONSUL_VER}_web_ui.zip
/tmp/webui.zip  
RUN mkdir /ui && cd /ui && unzip /tmp/webui.zip && rm /tmp/webui.zip && mv
dist/* . && rm -rf dist  
  
RUN opkg-install curl ca-certificates  
  
RUN cat /etc/ssl/certs/*.crt > /etc/ssl/certs/ca-certificates.crt && \  
sed -i -r '/^#.+/d' /etc/ssl/certs/ca-certificates.crt  
  
ADD ./config /config/  
ONBUILD ADD ./config /config/  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53/udp  
VOLUME ["/data"]  
  
ENTRYPOINT ["/bin/consul", "agent", "-config-dir=/config"]  
CMD []  

