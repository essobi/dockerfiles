FROM gliderlabs/alpine  
ENV CONSUL_VERSION 0.15.0  
ENV CONSUL_FILE_NAME consul-template_${CONSUL_VERSION}_linux_amd64.zip  
RUN apk add --update wget  
RUN wget --no-check-certificate http://releases.hashicorp.com/consul-
template/${CONSUL_VERSION}/${CONSUL_FILE_NAME} && \  
unzip ${CONSUL_FILE_NAME}  
ENTRYPOINT ["./consul-template"]  

