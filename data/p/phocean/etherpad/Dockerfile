FROM ubuntu:bionic  
  
MAINTAINER Phocean <jc@phocean.net>  
  
# install dir  
WORKDIR /opt  
  
# base  
RUN apt-get update &&\  
apt-get -y install gzip git-core curl python libssl-dev pkg-config build-
essential nodejs npm python3-pip &&\  
pip3 install dumb-init &&\  
npm install sqlite3 ep_headings ep_monospace_default ep_print &&\  
rm -rf /var/lib/apt/lists/*  
  
# get and install nodejs  
#RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
#RUN apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*  
# get dumb-init, to have nodejs app terminate properly (signal handling)  
#RUN curl -sL -O https://github.com/Yelp/dumb-
init/releases/download/v1.0.2/dumb-init_1.0.2_amd64.deb && dpkg -i dumb-
init_*.deb && rm dumb-init_*.deb  
# get and install etherpad  
RUN git clone git://github.com/ether/etherpad-lite.git &&\  
sed '/installDeps.sh/d' etherpad-lite/bin/run.sh -i &&\  
useradd -c "Etherpad user" -d /dev/null -s /bin/false etherpad &&\  
chown -R etherpad:etherpad . &&\  
/opt/etherpad-lite/bin/installDeps.sh  
  
# push our config file (simple sqlite config)  
ADD config/ /opt/etherpad-lite/  
  
# data volume for persistency of pads  
VOLUME /opt/etherpad-lite/var  
  
WORKDIR /opt/etherpad-lite/bin  
  
# startup script  
ADD run-docker.sh /opt/etherpad-lite/bin/  
CMD ["/opt/etherpad-lite/bin/run-docker.sh"]  

