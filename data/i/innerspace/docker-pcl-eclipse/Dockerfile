FROM innerspace/docker-pcl:ubuntu_16.04  
MAINTAINER Matt MacGillivray  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \  
apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer libxext-dev libxrender-dev libxtst-
dev sudo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
# Install libgtk as a separate step so that we can share the layer above with  
# the netbeans image  
RUN apt-get update && apt-get install -y libgtk2.0-0 libcanberra-gtk-module  
  
RUN wget -nv
http://mirror.csclub.uwaterloo.ca/eclipse/technology/epp/downloads/release/neon/3/eclipse-
cpp-neon-3-linux-gtk-x86_64.tar.gz -O /tmp/eclipse.tar.gz -q && \  
echo 'Installing eclipse' && \  
tar -xf /tmp/eclipse.tar.gz -C /opt && \  
rm /tmp/eclipse.tar.gz  
  
  
RUN mkdir -p /home/developer && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown developer:developer -R /home/developer && \  
chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo  
#RUN chmod +x /usr/local/bin/eclipse  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
#ADD run /opt/eclipse/eclipse  
CMD /opt/eclipse/eclipse  

