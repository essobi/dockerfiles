FROM ubuntu:trusty  
  
ENV MYUID 1000  
ENV MYGID 1000  
RUN apt-get update && apt-get install -y --force-yes wget apt-transport-https  
  
RUN wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub | sudo apt-
key add -  
  
RUN echo "deb http://mirror.oxfordnanoportal.com/apt trusty-stable non-free" |
sudo tee /etc/apt/sources.list.d/nanoporetech.sources.list  
  
RUN apt-get update && \  
apt-get install -y libgtk2.0 libxss1 libxtst6 libnss3 libgconf-2-4 libasound2
minknow-map || :  
RUN apt-get install -y -f  
  
RUN export uid=$MYUID gid=$MYGID && \  
mkdir -p /home/minion && \  
echo "minion:x:${uid}:${gid}:minion,,,:/home/minion:/bin/bash" >> /etc/passwd
&& \  
echo "minion:x:${uid}:" >> /etc/group && \  
echo "minion ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/minion && \  
chmod 0440 /etc/sudoers.d/minion && \  
chown ${uid}:${gid} -R /home/minion  
  
RUN ln -s /home/minion /opt/ONT/MinKNOW/reads  
  
USER minion  
ENV HOME /home/minion  
  
CMD /opt/ONT/MinKNOW/Client/MinKNOW  

