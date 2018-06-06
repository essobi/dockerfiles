FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y nodejs npm  
RUN npm install -g coffee-script  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
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

