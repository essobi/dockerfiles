FROM alpine  
MAINTAINER Shusui Moyatani  
  
ARG server_dir=/srv/minecraft  
ARG exec_user=minecraft  
ARG launcher_dir=/usr/local/bin/  
  
# Minecraft Port  
EXPOSE 25565  
  
# Install required packages and create group and user  
USER root  
RUN apk --update add openjdk8-jre \  
&& addgroup -g 1000 ${exec_user} \  
&& adduser -H -D -G ${exec_user} -u 1000 ${exec_user} \  
&& mkdir -p ${server_dir} \  
&& chown ${exec_user}:${exec_user} ${server_dir}  
# add launcher script  
ADD launcher.sh /usr/local/bin/minecraft_launcher.sh  
  
# Mountpoints: Settings files and Minecraft directory  
VOLUME ["${server_dir}"]  
  
# exec program  
USER ${exec_user}  
WORKDIR ${server_dir}  
STOPSIGNAL TERM  
ENTRYPOINT ["/usr/local/bin/minecraft_launcher.sh"]  

