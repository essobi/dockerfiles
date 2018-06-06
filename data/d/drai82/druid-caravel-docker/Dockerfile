# Ubuntu 12.04 (Precise Pangolin)  
FROM ubuntu:12.04  
# Download latest package list (required)  
RUN apt-get update  
  
# Install add-apt-repository utility  
RUN apt-get -y install python-software-properties  
  
# Automagically accept Oracle's license (for oracle-java8-installer)  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Install Java8  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install -y oracle-java8-installer  
  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get install -y curl && \  
apt-get install -y supervisor && \  
apt-get install -y build-essential libssl-dev libffi-dev python-dev python-pip
libsasl2-dev libldap2-dev python-six  
  
RUN pip install virtualenv  
# RUN pip install --upgrade setuptools pip  
RUN pip install superset  
RUN virtualenv venv  
  
RUN useradd -U druid && mkdir -p /home/druid/  
  
ENV tmpdir /tmp  
ENV home /home/druid/  
  
EXPOSE 8081  
EXPOSE 8082  
EXPOSE 8083  
EXPOSE 8088  
EXPOSE 8090  
EXPOSE 3306  
EXPOSE 2181 2888 3888  
# Download and run zookeeper  
RUN cd ${tmpdir} && \  
wget
http://www.gtlib.gatech.edu/pub/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
&& \  
tar -xzf zookeeper-3.4.6.tar.gz && \  
cp -r zookeeper-3.4.6 ${home}/ && \  
cp ${home}/zookeeper-3.4.6/conf/zoo_sample.cfg
${home}/zookeeper-3.4.6/conf/zoo.cfg && \  
cd ${home}/zookeeper-3.4.6  
  
RUN rm -rf ${tmpdir}/zookeeper-3.4.6.tar.gz ${tmpdir}/zookeeper-3.4.6  
  
# Download druid 0.8.3  
RUN cd ${tmpdir} && \  
wget http://static.druid.io/artifacts/releases/druid-0.8.3-bin.tar.gz && \  
tar -zxvf druid-0.8.3-bin.tar.gz && \  
cp -r druid-0.8.3 ${home} && \  
mkdir -p ${home}/druid-0.8.3/logs/  
  
RUN rm -rf ${tmpdir}/druid-0.8.3-bin.tar.gz ${tmpdir}/druid-0.8.3  
  
RUN cd ${home}/druid-0.8.3  
  
# Copying files  
ADD files/druid_files/run_druid_server.sh ${home}/druid-0.8.3/  
  
RUN chmod +x ${home}/druid-0.8.3/run_druid_server.sh  
  
RUN echo "druid.extensions.coordinates=[\"io.druid.extensions:druid-
datasketches\"]" >>
${home}/druid-0.8.3/config/_common/common.runtime.properties  
  
RUN mkdir -p ${home}/druid-0.8.3/extensions-repo/io/druid/extensions/druid-
datasketches/0.8.3/  
  
ADD files/druid_files/druid-datasketches/* ${home}/druid-0.8.3/extensions-
repo/io/druid/extensions/druid-datasketches/0.8.3/  
  
RUN mkdir -p ${home}/sample_data  
ADD files/sample_data/* ${home}/sample_data/  
  
## Create an admin user (you will be prompted to set username, first and last
name before setting a password)  
#RUN fabmanager create-admin --app superset  
RUN mkdir -p /root/.superset/  
ADD files/caravel_files/superset.db /root/.superset/superset.db  
  
## Initialize the database  
RUN superset db upgrade  
  
## Load some data to play with  
RUN superset load_examples  
  
## Create default roles and permissions  
RUN superset init  
  
# Setup supervisord  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENTRYPOINT export HOSTIP="$(resolveip -s $HOSTNAME)" && exec
/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf  

