FROM alpine  
  
MAINTAINER Antoine Dewaele "antoinee.dewaele@gmail.com"  
# installation  
RUN apk update && apk upgrade && apk add --no-cache openjdk8 wget sudo git
tmux bash  
  
# environment variable  
ENV VERSION='1.10.2'  
ENV MIN_MEM='512'  
ENV MAX_MEM='1024'  
ENV NB_THREAD='4'  
ENV SERVER_DIR=/home/minecraft  
  
# Copy script  
COPY scripts/install /usr/bin/  
COPY scripts/start /usr/bin/  
COPY scripts/stop /usr/bin/  
COPY scripts/reboot /usr/bin/  
COPY scripts/properties /usr/bin/  
COPY scripts/whitelist /usr/bin/  
COPY scripts/ops /usr/bin/  
COPY scripts/ban /usr/bin  
COPY scripts/banip /usr/bin  
  
# Create user  
RUN adduser -s /bin/false -D minecraft  
USER minecraft  
  
WORKDIR /home/minecraft/  
  
# Create volume  
VOLUME ["/var/docker/minecraft:/home/minecraft/"]  
  
ENTRYPOINT ["/bin/sh"]  
  
# port  
EXPOSE 25565

