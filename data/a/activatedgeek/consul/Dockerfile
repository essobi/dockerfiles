FROM alpine:latest  
  
MAINTAINER Sanyam Kapoor "1sanyamkapoor@gmail.com"  
RUN apk update &&\  
apk add --update curl &&\  
curl https://releases.hashicorp.com/consul/0.7.0/consul_0.7.0_linux_amd64.zip
-o consul_0.7.0_linux_amd64.zip &&\  
unzip consul_0.7.0_linux_amd64.zip &&\  
rm consul_0.7.0_linux_amd64.zip &&\  
mv consul /bin/consul &&\  
chmod a+x /bin/consul &&\  
mkdir -p /opt/consul/server/conf.d /opt/consul/agent/conf.d &&\  
apk del openssl libssh2 curl  
  
ADD scripts/docker-entrypoint.sh /docker-entrypoint.sh  
  
# export ports for various purposes if needed  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
ENTRYPOINT ["/bin/sh", "/docker-entrypoint.sh"]  
  
# sample CMDs for Docker run or for usage during a base image  
# CMD ["server", "127.0.0.1"]  
# CMD ["agent", "127.0.0.1"]  

