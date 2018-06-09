FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get -yy install software-properties-common sudo \  
supervisor x11vnc xvfb wget unzip openbox \  
lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6 firefox\  
qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils && rm -rf /var/run/cache  
RUN add-apt-repository -y ppa:openjdk-r/ppa  
RUN apt-get update  
RUN apt-get install openjdk-8-jdk -y && rm -rf /var/run/cache  
RUN wget https://dl.google.com/dl/android/studio/ide-zips/2.2.2.0/android-
studio-ide-145.3360264-linux.zip -O android-studio.zip  
RUN unzip -d /opt android-studio.zip && rm -rf android-studio.zip
/var/run/cache  
ADD etc /etc  
RUN adduser -q ubuntu \  
&& echo "ubuntu:ubuntu" | /usr/sbin/chpasswd \  
&& echo "ubuntu ALL=(ALL) ALL" >> /etc/sudoers \  
&& chown -R ubuntu:ubuntu /home/ubuntu  
WORKDIR /home/ubuntu  
USER ubuntu  
EXPOSE 5900  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  

