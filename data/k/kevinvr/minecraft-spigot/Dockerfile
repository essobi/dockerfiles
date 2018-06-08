# Minecraft spigot server latest dockerfile  
# AlpineLinux with java 8 jre  
FROM java:8-jre-alpine  
MAINTAINER Kevin Van Raepenbusch <metalleke@gmail.com>  
  
# Update certificates, install bash and git  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates \  
&& apk add bash \  
&& apk add git \  
&& rm -rf /var/cache/apk/*  
  
# Environment variables  
ENV REV latest  
ENV JVM_OPTS -Xmx1024M -Xms1024M -XX:+UseConcMarkSweepGC  
ENV SPIGOT_HOME /minecraft  
  
# Create folder for server files  
RUN mkdir ${SPIGOT_HOME}  
  
# Sets working directory for the CMD instruction (also works for RUN,
ENTRYPOINT commands)  
# Create mount point, and mark it as holding externally mounted volume  
WORKDIR ${SPIGOT_HOME}  
VOLUME ${SPIGOT_HOME}  
  
# Add installation script and make it runnable  
COPY ./install.sh install.sh  
RUN chmod +x install.sh  
  
# Expose the container's network port: 25565 during runtime.  
EXPOSE 25565  
# Run command  
CMD /bin/bash install.sh

