FROM ubuntu:latest  
  
RUN apt-get update -y && \  
apt-get install -y firefox && \  
apt-get clean -y  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
mkdir -p /etc/sudoers.d && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
CMD /usr/bin/firefox  

