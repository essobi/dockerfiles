FROM java:7-jdk  
MAINTAINER Robert Wallis <smilingrob@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y sudo && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget https://d1opms6zj7jotq.cloudfront.net/idea/ideaIC-15.0.4.tar.gz -O
/tmp/idea.tar.gz -q && \  
mkdir -p /usr/share/intellij && \  
tar -xf /tmp/idea.tar.gz --strip-components=1 -C /usr/share/intellij && \  
rm /tmp/idea.tar.gz  
  
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
VOLUME /tmp/.X11-unix  
  
CMD /usr/share/intellij/bin/idea.sh  

