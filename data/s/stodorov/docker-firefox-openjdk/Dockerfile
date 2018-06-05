FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y software-properties-common python-software-properties \  
&& add-apt-repository ppa:mozillateam/ppa \  
&& apt-get update \  
&& apt-get install -y firefox-esr openjdk-8-jre icedtea-8-plugin  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 \  
&& mkdir -p /home/developer \  
&& echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd \  
&& echo "developer:x:${uid}:" >> /etc/group \  
&& echo "developer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& chown ${uid}:${gid} -R /home/developer \  
&& rm -rf /var/lib/apt/lists/*  
  
USER developer  
  
ENV HOME /home/developer  

