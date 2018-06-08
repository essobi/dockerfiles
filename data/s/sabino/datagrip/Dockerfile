FROM phusion/baseimage  
MAINTAINER Felipe Sabino "fgsabino@gmail.com"  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \  
apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer oracle-java7-installer libxext-dev
libxrender-dev libxtst-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN apt-get update && apt-get install -y libgtk2.0-0 libcanberra-gtk-module
sudo  
  
RUN wget https://download.jetbrains.com/datagrip/datagrip-2016.2.6.tar.gz -O
/tmp/datagrip.tar.gz -q && \  
echo 'Installing datagrip' && \  
tar -xf /tmp/datagrip.tar.gz -C /opt && \  
mv /opt/DataGrip-2016.2.6 /opt/datagrip && \  
rm /tmp/datagrip.tar.gz && \  
ln -s /opt/datagrip/bin/datagrip.sh /usr/local/bin/datagrip  
  
RUN chmod +x /usr/local/bin/datagrip && \  
mkdir -p /home/developer && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown -R developer:developer /home/developer && \  
chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo  
  
RUN echo 'rm -rf /home/developer/.DataGrip2016.2.6/config/eval' >>
/usr/local/bin/dataGripNewLicense && \  
chmod +x /usr/local/bin/dataGripNewLicense  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
CMD /usr/local/bin/dataGripNewLicense && /usr/local/bin/datagrip  

