#  
# Etherpad lite Dockerfile  
#  
# Based on instructions from https://github.com/ether/etherpad-lite  
#  
FROM dockerfile/nodejs  
  
MAINTAINER Johannes Bornhold <johannes@bornhold.name>  
  
  
# Prepare etherpad  
RUN mkdir /src  
WORKDIR /src  
  
# Dependencies based on docs  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \  
gzip git-core curl python libssl-dev pkg-config build-essential  
  
RUN wget https://github.com/ether/etherpad-lite/archive/master.zip &&\  
unzip master &&\  
rm -f master.zip &&\  
mv etherpad-lite-master etherpad &&\  
sed '/installDeps.sh/d' etherpad/bin/run.sh -i  
  
WORKDIR /src/etherpad  
  
# Install dependencies  
RUN bin/installDeps.sh  
RUN npm install sqlite3  
  
# Add the settings  
ADD config/ /src/etherpad/  
  
# Install plugins  
RUN npm install \  
ep_headings \  
ep_monospace_default \  
ep_print  
  
EXPOSE 9001  
VOLUME ["/data"]  
  
CMD ["bin/configure_and_run.sh"]  

