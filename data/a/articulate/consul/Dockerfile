FROM alpine:3.2  
ENV CONSUL_VERSION 0.7.5  
ENV CONSUL_SHA256
40ce7175535551882ecdff21fdd276cef6eaab96be8a8260e0599fadb6f1f5b8  
  
RUN apk --update add curl ca-certificates && \  
rm -rf /var/cache/apk/*  
  
ADD
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
/tmp/consul.zip  
  
RUN echo "${CONSUL_SHA256} /tmp/consul.zip" > /tmp/consul.sha256 \  
&& sha256sum -c /tmp/consul.sha256 \  
&& cd /bin \  
&& unzip /tmp/consul.zip \  
&& chmod +x /bin/consul \  
&& rm /tmp/consul.zip  
  
ENTRYPOINT ["/bin/consul"]  

