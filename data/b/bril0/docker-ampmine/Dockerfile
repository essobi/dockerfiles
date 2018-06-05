FROM linuxserver/baseimage  
MAINTAINER James Littler <brilosoft@gmail.com>  
ENV APTLIST="oracle-java7-installer oracle-java7-set-default wget zip unzip
git-core lib32gcc1 coreutils screen socat"  
#Env Vars for module creation  
ENV AMP_LICENCE=your_license_here  
ENV PASSWORD=Password  
ENV MOD_NAME=Miner  
  
#Applying stuff  
RUN add-apt-repository ppa:webupd8team/java && \  
apt-get update -q && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
sudo /usr/bin/debconf-set-selections && \  
apt-get install $APTLIST -y && \  
wget https://www.cubecoders.com/Downloads/ampinstmgr.zip -O
/tmp/ampinstmgr.zip && \  
#wget http://mcmyadmin.com/Downloads/etc.zip -O /tmp/etc.zip && \  
#unzip /tmp/etc.zip -d /usr/local && \  
unzip /tmp/ampinstmgr.zip -d /tmp && \  
rm /tmp/ampinstmgr.zip && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/*  
  
#Adding Custom files  
ADD init/ /etc/my_init.d/  
RUN chmod -v +x /etc/my_init.d/*.sh #ADD services/ /etc/service/ #RUN chmod -v
+x /etc/service/*/run &&  
  
# Volums and Ports  
VOLUME /minecraft  
EXPOSE 8080  
EXPOSE 25565  

