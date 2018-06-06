FROM alpine:3.4  
RUN apk --update add ca-certificates wget  
RUN wget -O /tmp/consul-template.zip https://releases.hashicorp.com/consul-
template/0.12.0/consul-template_0.12.0_linux_amd64.zip && \  
unzip /tmp/consul-template.zip -d /usr/local/bin/ && \  
rm /tmp/consul-template.zip && \  
mkdir /templates /output  
VOLUME ["/templates", "/output"]  
ENTRYPOINT ["consul-template"]ENTRYPOINT ["/bin/consul-template"]  

