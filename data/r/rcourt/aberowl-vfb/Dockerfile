FROM ubuntu:16.04  
# Install requirements:  
RUN apt-get -qq -y update && \  
apt-get -qq -y install coreutils nodejs nodejs-legacy npm apache2 build-
essential chrpath libssl-dev libxft-dev openjdk-8-jdk \  
libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev curl wget git
zip unzip bash sed  
  
WORKDIR /opt  
ENV SDKMAN_DIR=/opt/.sdkman  
ENV VFBOWL_VER=Current  
  
#update npm  
RUN npm install -g npm@5.1.0  
  
# Install phantomjs  
RUN cd /opt && \  
wget
http://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/ && \  
ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin/  
  
# Install redis  
RUN cd /opt && \  
wget http://download.redis.io/redis-stable.tar.gz && \  
tar xvzf redis-stable.tar.gz && \  
cd redis-stable && \  
cd deps && \  
ls -d * | xargs make && \  
cd .. && \  
make && \  
make install  
  
#Start redis  
RUN cd /opt/redis-stable/utils && \  
echo -n | ./install_server.sh  
  
# Install AberOWL  
RUN cd /opt && \  
git clone https://github.com/bio-ontology-research-group/aberowl-meta  
COPY install /opt/aberowl-meta/install  
RUN cd /opt/aberowl-meta/ && \  
./install  
RUN cd /opt/aberowl-meta/aberowl-web && \  
npm install jsdom && \  
npm install xmlhttprequest && \  
npm install databank && \  
npm install phantomjs && \  
npm install phantom && \  
npm install xmldom && \  
npm install cache-manager  
RUN cd /opt/aberowl-meta/aberowl-web/node_modules/databank/ && \  
npm install databank-redis  
  
RUN apt-get -qq -y clean  
  
EXPOSE 31337  
RUN mkdir -p /opt/aberowl-meta/ontologies/VFB/new && \  
ln -s /opt /home/hohndor && \  
mkdir -p /opt/aberowl-meta/ontologies/VFB/release  
COPY config.json /opt/aberowl-meta/ontologies/VFB/config.json  
  
# Create server start script  
COPY runservers.sh /opt/runservers.sh  
RUN chmod +x /opt/runservers.sh && \  
cat /opt/runservers.sh  
  
# Create SDK dir accessible  
RUN chmod -R 777 /opt  
  
RUN curl -s get.sdkman.io | bash - && \  
chmod -R 777 /opt && \  
/bin/bash -c "source /opt/.sdkman/bin/sdkman-init.sh; sdk install groovy"  
  
# correct db prefix  
RUN sed -i "s|DB_PREFIX = 'ontos:'|DB_PREFIX = 'ontologies:'|" /opt/aberowl-
meta/jenkins/workspace/*.groovy  
  
# Link initial ontology  
RUN ln -s /opt/aberowl-meta/ontologies/VFB/release/VFB_1.ont /opt/aberowl-
meta/aberowl-server/onts/  
  
# correct server port:  
RUN sed -i "s|String ABEROWL_API = 'http://localhost:30000/api/'|String
ABEROWL_API = 'http://localhost:31337/api/'|" /opt/aberowl-
meta/jenkins/workspace/Restart.groovy  
  
# start AberOWL servers:  
ENTRYPOINT ["/opt/runservers.sh"]  
  
CMD ["/bin/bash"]  

