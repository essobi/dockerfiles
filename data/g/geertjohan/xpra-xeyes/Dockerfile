FROM geertjohan/xpra  
  
# Install xeyes  
RUN sudo apt-get update && sudo apt-get -y install --no-install-recommends
x11-apps  
  
# Add simple user to drop permissions to  
# TODO: better way to create a user?  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/user && \  
echo "user:x:${uid}:${gid}:User,,,:/home/user:/bin/bash" >> /etc/passwd && \  
echo "user:x:${uid}:" >> /etc/group && \  
chown ${uid}:${gid} -R /home/user  
  
# cleanup  
RUN sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add init script and entrypoint  
ADD src/init.sh /usr/local/bin/init.sh  
ENTRYPOINT /usr/local/bin/init.sh  

