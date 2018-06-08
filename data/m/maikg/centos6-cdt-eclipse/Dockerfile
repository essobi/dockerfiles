FROM maikg/centos6-cdt  
RUN yum -y install sudo gtk2-engines openssh-server man man-pages firefox
boost-devel hicolor-icon-theme nuvola-icon-theme  
  
RUN rm -f /tmp/*tar.gz  
  
RUN wget http://ftp-stud.fht-
esslingen.de/pub/Mirrors/eclipse/technology/epp/downloads/release/oxygen/3a/eclipse-
cpp-oxygen-3a-linux-gtk-x86_64.tar.gz -O /tmp/eclipse.tar.gz && \  
echo 'Installing eclipse' && \  
tar -xf /tmp/eclipse.tar.gz -C /opt && \  
rm -f /tmp/eclipse.tar.gz  
  
RUN wget http://ftp-stud.hs-
esslingen.de/pub/Mirrors/ftp.apache.org/dist/maven/binaries/apache-
maven-3.1.1-bin.tar.gz -O /tmp/maven.tar.gz && \  
echo 'Installing maven 3.1.1' && \  
tar -xf /tmp/maven.tar.gz -C /opt && \  
rm -f /tmp/maven.tar.gz  
  
ADD run /usr/local/bin/eclipse  
  
RUN chmod +x /usr/local/bin/eclipse && \  
mkdir -p /home/developer && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown developer:developer -R /home/developer && \  
chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo && \  
mkdir /home/developer/.ssh && \  
chown developer:developer /home/developer/.ssh && \  
echo "ForwardX11 yes" > /home/developer/.ssh/config && \  
chown developer:developer /home/developer/.ssh/config && \  
chmod 0600 /home/developer/.ssh/config  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  

