FROM mhart/alpine-node:8.9.4  
ENV CONSUL_VERSION=0.9.2  
ENV ENVCONSUL_VERSION=0.7.1  
RUN apk add --update curl git && rm -rf /var/cache/apk/*  
  
# Install consul  
RUN curl -sL -o /tmp/consul.zip
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
&& \  
unzip /tmp/consul.zip -d /bin && \  
chmod +x /bin/consul && \  
rm /tmp/consul.zip  
  
# Install envconsul  
RUN curl -sL -o /tmp/envconsul.zip
https://releases.hashicorp.com/envconsul/${ENVCONSUL_VERSION}/envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip
&& \  
unzip /tmp/envconsul.zip -d /bin && \  
chmod +x /bin/envconsul && \  
rm /tmp/envconsul.zip  
  
# Register consul init.d  
COPY consul.init.d /etc/init.d/consul  
RUN chmod 755 /etc/init.d/consul  
  
EXPOSE 8301 8301/udp  
  
ENTRYPOINT ["node"]  

