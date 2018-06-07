FROM elementary/docker:loki  
  
RUN add-apt-repository ppa:philip.scott/notes-up && \  
apt-get update && \  
apt-get install -y com.github.philip-scott.notes-up  
  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/user && \  
mkdir /etc/sudoers.d/ && \  
echo "user:x:${uid}:${gid}:User,,,:/home/user:/bin/bash" >> /etc/passwd && \  
echo "user:x:${uid}:" >> /etc/group && \  
echo "user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/user && \  
chmod 0440 /etc/sudoers.d/user && \  
chown ${uid}:${gid} -R /home/user  
  
RUN mkdir -p /media/user/home && mkdir -p /media/user/current  
  
USER user  
ENV HOME /home/user  
  
CMD /usr/bin/notes-up  

