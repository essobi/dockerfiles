FROM openjdk:8-jdk  
MAINTAINER Jeferson Mombach de Sousa <jefersonmombach@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y sudo && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget https://download.jetbrains.com/idea/ideaIC-2017.2.3-no-jdk.tar.gz -O
/tmp/idea.tar.gz -q && \  
mkdir -p /usr/share/intellij && \  
tar -xf /tmp/idea.tar.gz --strip-components=1 -C /usr/share/intellij && \  
rm /tmp/idea.tar.gz  
  
RUN export uid=2507 gid=2507 && \  
mkdir -p /home/developer && \  
mkdir -p /home/developer/src && \  
mkdir -p /home/developer/files && \  
mkdir -p /home/developer/temp && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
  
VOLUME ["/tmp/.X11-unix", "/home/developer/src", "/home/developer/files",
"/home/developer/temp"]  
  
CMD /usr/share/intellij/bin/idea.sh

