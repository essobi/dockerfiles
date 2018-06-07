FROM magneval/openjdk8  
  
MAINTAINER magneval  
  
#ENV HTTP_PROXY http://172.17.0.1:3128/  
RUN apt-get install -y software-properties-common libxext-dev libxrender-dev
libxtst-dev xterm  
RUN apt-get install -y jedit  
RUN apt-get install -y sudo  
  
RUN mkdir -p /home/developer && \  
mkdir -p /etc/sudoers.d && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer  
RUN echo "alias ll='ls -ail --color=auto' " >> /home/developer/.bashrc && \  
chown developer:developer -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
ADD jedit.tgz /home/developer  
  
RUN sudo chown developer:developer -R /home/developer  
  
CMD /usr/bin/jedit  
  

