from ubuntu:trusty  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
ENV REFRESHED_AT 2014-06-23  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN sed 's/us-east-1.ec2.archive.ubuntu.com/nova.clouds.archive.ubuntu.com/'
-i /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test  
RUN add-apt-repository ppa:fkrull/deadsnakes  
RUN apt-get update  
  
RUN apt-get install -y build-essential \  
curl \  
c++-4.7 \  
dpkg \  
git \  
g++-4.7 \  
librtmp0 \  
libssl0.9.8 \  
lsb-release \  
npm \  
openjdk-7-jdk \  
pwgen \  
python2.7 \  
python-mysqldb \  
python-setuptools \  
wget \  
zip  
RUN easy_install pip  
RUN pip install texttable \  
requests \  
six==1.5.2 \  
pyes \  
pdfminer==20110515 \  
xlrd==0.9.2 \  
xmltodict==0.5.0 \  
python-magic==0.4.3  
RUN npm config set registry http://registry.npmjs.org/  
RUN npm install tty.js  
  
# elasticsearch  
RUN wget --no-check-certificate
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.2.deb  
RUN dpkg -i elasticsearch-0.90.2.deb  
RUN /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head  
RUN echo 'discovery.zen.ping.multicast.enabled: false' >>
/etc/elasticsearch/elasticsearch.yml; \  
echo 'node.local: false' >> /etc/elasticsearch/elasticsearch.yml; \  
echo 'index.number_of_shards: 1' >> /etc/elasticsearch/elasticsearch.yml; \  
echo 'index.number_of_replicas: 0' >> /etc/elasticsearch/elasticsearch.yml; \  
echo 'script.disable_dynamic: true' >> /etc/elasticsearch/elasticsearch.yml  
  
# couchbase  
ENV CB_VERSION 2.0.1  
ENV CB_DOWNLOAD_URL http://packages.couchbase.com/releases  
ENV CB_PACKAGE couchbase-server-community_x86_64_$CB_VERSION.deb  
ENV CB_USERNAME Administrator  
ENV CB_PASSWORD password  
  
# install jq for parsing json  
RUN wget http://stedolan.github.io/jq/download/linux64/jq  
RUN chmod +x ./jq  
RUN cp jq /usr/bin  
  
# Limits  
RUN sed -i.bak '/\\# End of file/ i\\\\# Following 4 lines added by docker-
couchbase-server' /etc/security/limits.conf  
RUN sed -i.bak '/\\# End of file/ i\\\\* hard memlock unlimited'
/etc/security/limits.conf  
RUN sed -i.bak '/\\# End of file/ i\\\\* soft memlock unlimited\n'
/etc/security/limits.conf  
RUN sed -i.bak '/\\# End of file/ i\\\\* hard nofile 65536'
/etc/security/limits.conf  
RUN sed -i.bak '/\\# End of file/ i\\\\* soft nofile 65536\n'
/etc/security/limits.conf  
RUN sed -i.bak '/\\# end of pam-auth-update config/ i\\\\# Following line was
added by docker-couchbase-server' /etc/pam.d/common-session  
RUN sed -i.bak '/\\# end of pam-auth-update config/ i\session required
pam_limits.so\n' /etc/pam.d/common-session  
  
# sets root password to password, but isn't accessible from the outside  
RUN echo 'mysql-server-5.5 mysql-server/root_password password password' |
debconf-set-selections  
RUN echo 'mysql-server-5.5 mysql-server/root_password_again password password'
| debconf-set-selections  
RUN apt-get install -y mysql-server --fix-missing --fix-broken && apt-get
clean && rm -rf /var/lib/apt/lists/*  
  
ENV HEMLOCK_PULLED_AT 2014-06-23  
RUN git clone https://github.com/Lab41/Hemlock.git  
RUN cd /Hemlock; python setup.py install  
  
# kibana  
RUN git clone https://github.com/elasticsearch/kibana.git  
RUN cd /kibana; git checkout 322fa427ab  
ADD config.js /kibana/src/  
ADD default.json /kibana/src/app/dashboards/default.json  
  
# Download Couchbase Server package to /tmp & install  
ADD $CB_DOWNLOAD_URL/$CB_VERSION/$CB_PACKAGE /tmp/$CB_PACKAGE  
RUN dpkg -i /tmp/$CB_PACKAGE  
RUN ln -s /opt/couchbase/bin/couchbase-cli /usr/local/bin/  
  
# Put start script  
ADD couchbase-start /usr/local/bin/  
  
ADD . /src  
  
# data  
RUN mkdir /Hemlock/data  
RUN tar xfz /src/data.tar.gz -C /Hemlock/data/  
  
# tty.js  
ADD favicon.ico /node_modules/tty.js/static/favicon.ico  
ADD index.html /node_modules/tty.js/static/index.html  
ADD tty.js /node_modules/tty.js/bin/tty.js  
  
# couchbase plugin with elasticsearch  
RUN mkdir /usr/share/elasticsearch/plugins/transport-couchbase  
RUN unzip /src/elasticsearch-transport-couchbase-1.1.0.zip -d
/usr/share/elasticsearch/plugins/transport-couchbase  
RUN cp /src/couchbase_template.json
/usr/share/elasticsearch/plugins/transport-couchbase/couchbase_template.json  
  
# add rsyslog  
RUN sed 's/#\$ModLoad imudp/\$ModLoad imudp/' -i /etc/rsyslog.conf  
RUN sed 's/#\$UDPServerRun 514/\$UDPServerRun 514/' -i /etc/rsyslog.conf  
  
RUN groupadd docker  
RUN useradd -m -d /home/docker -g docker docker  
RUN touch /etc/rsyslog.d/50-default.conf  
RUN chsh -s /bin/bash docker  
RUN chown -R docker /home/docker /Hemlock /etc/rsyslog.d/50-default.conf  
  
EXPOSE 8000 9200  
CMD printf "*.*\t@$REMOTE_HOST" >> /etc/rsyslog.d/50-default.conf; \  
/etc/init.d/rsyslog start; \  
logger started hemlock container $PARENT_HOST; \  
su -c '/node_modules/tty.js/bin/tty.js --port 8000 --daemonize' \- docker && \  
/src/startup.sh  

