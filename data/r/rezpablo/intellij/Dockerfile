FROM rezpablo/ubuntu_java8  
  
RUN wget http://download.jetbrains.com/idea/ideaIU-15.0.1.tar.gz -O
/tmp/intellij.tar.gz -q && \  
mkdir -p /opt/intellij && \  
tar -xf /tmp/intellij.tar.gz --strip-components=1 -C /opt/intellij && \  
rm /tmp/intellij.tar.gz  
  
ADD run /usr/local/bin/intellij  
  
RUN chmod +x /usr/local/bin/intellij && \  
mkdir -p /home/developer && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown developer:developer -R /home/developer && \  
chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo  
  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y libxext-dev libxrender-dev libxtst-dev  
RUN apt-get update && apt-get install -y libgtk2.0-0 libcanberra-gtk-module  
RUN rm -rf /var/lib/apt/lists/*  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
CMD /usr/local/bin/intellij  

