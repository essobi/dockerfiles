FROM ubuntu:14.04  
MAINTAINER Nicolas Lemahieu <nicolas.lemahieu@sensiolabs.com>  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y nodejs npm && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
npm install -g yo bower grunt-cli gulp --save-dev && \  
npm install -g generator-angular --save-dev  
  
# Replace 1000 / 1000 by your user id and group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /project

