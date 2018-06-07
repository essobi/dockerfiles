FROM alpine  
  
LABEL maintainer "Feng Zhou <feng.zh@gmail.com>"  
  
COPY . /src  
  
RUN /src/docker/docker-build.sh  
  
ENV LISTEN_PORT=3129 HTTP_PROXY="" NO_PROXY="127.0.0.1/8" IPTABLE_MARK="5"
PROXY_PORTS="80,443" VERBOSE=false DNS_PORT=0 PROXY_CONFIG_FILE=  
  
CMD ["/bin/start-any-proxy.sh"]  

