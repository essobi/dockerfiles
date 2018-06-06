FROM alpine  
RUN apk --no-cache add curl zip && \  
curl https://releases.hashicorp.com/consul/0.6.3/consul_0.6.3_linux_amd64.zip
> /tmp/consul.zip && \  
unzip /tmp/consul.zip -o -d /bin && \  
rm /tmp/consul.zip  
CMD ["consul"]  
  

