FROM ubuntu  
LABEL vendor="MyHush"  
  
RUN apt-get update && \  
apt-get -y install wget apt-utils apt-transport-https git default-jdk ant && \  
echo 'deb https://dl.bintray.com/myhush/hush/ hush main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
379CE192D401AB61 && \  
apt-get update && \  
apt-get -y install hush && \  
rm -rf /var/lib/apt/lists/* && apt-get clean  
  
RUN mkdir -p /root/.hush && \  
echo "rpcuser=HushUserNow" >> /root/.hush/hush.conf && \  
echo "rpcpassword=`head -c 32 /dev/urandom | base64`" >> /root/.hush/hush.conf
&& \  
echo "addnode=myhush.network" >> /root/.hush/hush.conf && \  
echo "addnode=us.madmining.club" >> /root/.hush/hush.conf && \  
hush-fetch-params  
  
RUN git clone https://github.com/vaklinov/hush-swing-wallet-ui.git && \  
cd hush-swing-wallet-ui/ && \  
ant -buildfile ./src/build/build.xml && \  
chmod u+x ./build/jars/HUSHSwingWalletUI.jar  
  
CMD java -jar hush-swing-wallet-ui/build/jars/HUSHSwingWalletUI.jar  
  
# donations: t1NFhdY1tAGFt3nshjsY4vF1VjeYVhyjNNV  

