FROM ubuntu:16.04  
  
RUN apt-get update  
RUN apt-get install -y nodejs npm git sudo curl  
RUN ln -s "$(which nodejs)" /usr/bin/node  
RUN npm install -g gulp  
RUN npm install -g bower  
  
RUN mkdir -p /home/developer/ && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown developer:developer -R /home/developer  
  
USER developer  
CMD /bin/bash  

