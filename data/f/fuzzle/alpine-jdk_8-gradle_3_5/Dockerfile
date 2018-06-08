# This image is based on alpine:3.6 -> openjdk:8-jdk-alpine ->
gradle:3.5-jdk8-alpine  
# The following packages are installed by the base images:  
# openjdk8-jre, bash, libstdc++, ca-certificates, openssl, unzip  
# Packages installed by this Dockerfile:  
# curl, openssh, shadow, git, sudo  
FROM gradle:3.5-jdk8-alpine  
  
MAINTAINER Ali Bengali <ali-beng-ali@users.noreply.github.com>  
  
USER root  
  
# Install eclipse-che dependencies  
RUN cd && apk --update upgrade \  
&& apk add --no-cache \  
curl openssh shadow git sudo \  
&& deluser gradle \  
&& adduser -S user -s /bin/bash -G root -u 1000 \  
&& echo "%root ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& usermod -p "*" user \  
&& chown -R user /home/user/ \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 22 8000 8080  
WORKDIR /projects  
  
USER user  
CMD sudo /usr/bin/ssh-keygen -A && \  
sudo /usr/sbin/sshd -D && \  
sudo su - && \  
tail -f /dev/null  
  

