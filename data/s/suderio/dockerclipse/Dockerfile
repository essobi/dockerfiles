FROM suderio/ubuntu-java:8  
MAINTAINER Paulo Suderio "paulo.suderio@gmail.com"  
RUN apt-get update  
RUN apt-get install -y sudo wget  
RUN wget
http://eclipse.mirror.rafal.ca/eclipse/downloads/drops4/S-4.7M3-201610270700/eclipse-
platform-4.7M3-linux-gtk-x86_64.tar.gz -O /tmp/eclipse.tar.gz -q && \  
tar -xf /tmp/eclipse.tar.gz -C /opt && \  
rm /tmp/eclipse.tar.gz  
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
WORKDIR /home/developer  
RUN sudo apt-get update  
RUN sudo apt-get install libswt-gtk-3-java libcanberra-gtk3-module -y  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/* && \  
sudo rm -rf /tmp/*  
CMD /home/developer/eclipse/eclipse  
  

