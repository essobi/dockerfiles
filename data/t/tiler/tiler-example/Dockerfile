FROM library/ubuntu  
  
WORKDIR /tmp  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
add-apt-repository -y ppa:andrei-pozolotin/maven3 && \  
apt-get update && \  
apt-get install -y curl && \  
(curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -) && \  
apt-get install -y nodejs && \  
npm install -g grunt-cli && \  
apt-get install -y build-essential tcl8.5 wget && \  
wget http://download.redis.io/redis-stable.tar.gz && \  
tar xvzf redis-stable.tar.gz && \  
cd redis-stable && \  
make && \  
make install && \  
cd /tmp && \  
apt-get install -y oracle-java8-installer && \  
apt-get install -y maven && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
COPY . /tmp/tiler-example  
  
RUN \  
cd /tmp/tiler-example && \  
npm install && \  
grunt build && \  
mvn package && \  
mkdir /opt/tiler-example && \  
cp target/tiler-example-*-fat.jar /opt/tiler-example && \  
cp config.json /opt/tiler-example && \  
  
WORKDIR /opt/tiler-example  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
EXPOSE 8080  
  
CMD redis-server --daemonize yes && java -jar tiler-example-*-fat.jar -conf
config.json  

