  
# Usage:  
# sudo docker build --tag=derrickoswald/things .  
# interactive:  
# sudo docker run --tty --interactive --rm --name things --publish=6984:5984
--publish=9112:8112 derrickoswald/things  
# background:  
# sudo docker run --detach --name things --publish=6984:5984
--publish=9112:8112 derrickoswald/things /scripts/run.sh  
FROM ubuntu:trusty  
MAINTAINER Derrick Oswald <derrick.oswald@gmail.com>  
  
# Install utilities  
RUN locale-gen en_US.UTF-8 && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \  
sed --in-place 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install --assume-yes --force-yes \  
apt-transport-https \  
build-essential \  
curl \  
git \  
software-properties-common \  
wget  
  
# Install and configure CouchDB 1.6.0  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get install --assume-yes --force-yes \  
erlang-dev \  
erlang-manpages \  
erlang-base-hipe \  
erlang-eunit \  
erlang-nox \  
erlang-xmerl \  
erlang-inets \  
libmozjs185-dev \  
libicu-dev \  
libcurl4-gnutls-dev \  
libtool && \  
cd /tmp && \  
wget http://mirror.sdunix.com/apache/couchdb/source/1.6.0/apache-
couchdb-1.6.0.tar.gz && \  
tar xzvf apache-couchdb-1.6.0.tar.gz && \  
cd apache-couchdb-1.6.0 && \  
./configure && \  
make && \  
make install && \  
sed --expression 's/^bind_address = .*$/bind_address = 0.0.0.0/' \--in-place
/usr/local/etc/couchdb/default.ini && \  
sed --expression 's/^database_dir = .*$/database_dir = \/data/' \--in-place
/usr/local/etc/couchdb/default.ini && \  
sed --expression 's/^view_index_dir = .*$/view_index_dir = \/data/' \--in-
place /usr/local/etc/couchdb/default.ini && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Node.js v0.12  
# See https://nodesource.com/blog/nodejs-v012-iojs-and-the-nodesource-linux-
repositories  
RUN apt-get install --assume-yes --force-yes \  
g++ \  
make && \  
curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash - && \  
apt-get install --assume-yes --force-yes \  
nodejs && \  
npm config set prefix '/usr/local' && \  
npm install nano  
  
# Install Deluge  
# See http://dev.deluge-torrent.org/wiki/UserGuide/Service/Upstart  
RUN mkdir --parents /usr/local/etc/deluge && \  
apt-get update && \  
apt-get install --assume-yes --force-yes \  
deluged \  
deluge-webui  
  
# Download JDK 8u60 from Oracle download site  
ENV JAVA_DOWNLOAD_URL http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.tar.gz  
ENV JAVA_INSTALLATION_DIR /opt  
RUN curl --location "$JAVA_DOWNLOAD_URL" \--header "Cookie:
oraclelicense=accept-securebackup-cookie; gpw_e24=Dockerfile" | tar --extract
--gzip --directory=$JAVA_INSTALLATION_DIR && \  
ln --symbolic $JAVA_INSTALLATION_DIR/jdk1.8.0_60/bin/* /usr/local/bin/  
ENV JAVA_HOME $JAVA_INSTALLATION_DIR/jdk1.8.0_60  
  
# Install couchdb-lucene  
# See https://github.com/rnewson/couchdb-lucene/  
RUN apt-get install --assume-yes --force-yes \  
maven2 && \  
git clone https://github.com/rnewson/couchdb-lucene.git && \  
cd couchdb-lucene && \  
mvn && \  
cd .. && \  
unzip couchdb-lucene/target/couchdb-lucene-1.1.0-SNAPSHOT-dist.zip && \  
rm -rf /couchdb-lucene && \  
mv couchdb-lucene-1.1.0-SNAPSHOT couchdb-lucene && \  
rm -rf /root/.m2  
# add this step if you aren't running CouchDb in Admin Party mode:  
# sed --expression 's/url = http:\/\/localhost:5984/url =
http:\/\/admin:secret@localhost:5984/g' --in-place couchdb-
lucene-1.1.0-SNAPSHOT/conf/couchdb-lucene.ini  
# Add scripts  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh  
RUN touch /.firstrun  
ADD config/deluge /usr/local/etc/deluge/  
ADD logs/deluge /etc/logrotate.d/  
ADD js /js  
  
# Set environment variables  
ENV HOME /root  
  
# Define working directory  
WORKDIR /root  
  
# Define default command  
CMD ["bash"]  
  
# Command to run  
#ENTRYPOINT ["/scripts/run.sh"]  
#CMD [""]  
# Expose CouchDb listen port  
EXPOSE 5984  
# Expose web server port  
EXPOSE 8112  
# Expose our data, logs and configuration volumes  
VOLUME ["/data", "/usr/local/var/log/couchdb", "/usr/local/etc/couchdb"]  
VOLUME ["/torrents", "/usr/local/var/log/deluge", "/usr/local/etc/deluge"]  
  

