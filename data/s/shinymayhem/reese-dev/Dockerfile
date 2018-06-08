FROM shinymayhem/dev  
  
ADD run.sh /opt/deploy/run.sh  
ADD init-home.sh /opt/deploy/init-home.sh  
  
RUN \  
apt-get update && \  
apt-get install -y screen && \  
rm -rf /var/lib/apt/lists/* && \  
chmod +x /opt/deploy/*.sh && \  
useradd -m reese -s /bin/bash && \  
usermod -a -G admin reese  
  
USER reese  
  
RUN \  
cd /home/reese && \  
git clone http://github.com/shinymayhem/home && \  
cp -R home/. . && \  
echo 'so ~/.syncedvimrc' > .vimrc && \  
vim -E -u NONE -S ~/.vimrc +qall  
  
USER root  

