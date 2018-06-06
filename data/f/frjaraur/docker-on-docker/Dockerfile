FROM alpine:latest  
  
MAINTAINER frjaraur@gmail.com  
  
RUN apk --update --no-cache add git iptables curl xz python py-pip procps  
  
ADD https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz /tmp  
  
RUN tar -zxvf /tmp/docker-latest.tgz -C /tmp && mv /tmp/docker/* /bin \  
&& rm -rf /tmp/docker*  
  
RUN pip install docker-compose  
  
# Added if you want to use internal Docker Engine  
EXPOSE 2375  
# Added to allow dynamic port publishing  
EXPOSE 32768-65000  
ENTRYPOINT ["/bin/dockerd"]  
  
ENV DOCKER_HOST 0.0.0.0:2375  
CMD ["-D","-H","tcp://0.0.0.0:2375","-H", "unix://var/run/docker.sock"]  

