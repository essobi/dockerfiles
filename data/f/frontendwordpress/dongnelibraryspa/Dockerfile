FROM ubuntu:14.04  
# Replace 1000 with your user / group id  
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
ENV PS1 developer$  
WORKDIR /home/developer  
RUN sudo apt-get update && \  
sudo apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \  
sudo apt-get install -y nodejs && \  
sudo apt-get install -y git && \  
git clone https://github.com/afrontend/dongnelibraryspa /home/developer && \  
npm install  
CMD ["npm", "start"]  

