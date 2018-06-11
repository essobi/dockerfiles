FROM ubuntu:trusty  
  
# install oracle java 8  
RUN apt-get update && \  
apt-get -y install software-properties-common python-software-properties && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get -y install oracle-java8-installer  
  
# install git, vim, and some other dependencies  
RUN apt-get -y install git vim apt-transport-https curl adduser libfontconfig
openssh-server  
  
# will be working as 'jcconf' user, with password-less sudo access  
RUN useradd -m -s /bin/bash jcconf  
RUN echo "jcconf ALL= NOPASSWD: ALL" >> /etc/sudoers  
  
# install InfluxDB 0.12  
RUN wget https://s3.amazonaws.com/influxdb/influxdb_0.12.1-1_amd64.deb && \  
dpkg -i ./influxdb_0.12.1-1_amd64.deb && \  
rm influxdb_0.12.1-1_amd64.deb  
  
# install Grafana 3.1.1  
RUN wget
http://grafanarel.s3.amazonaws.com/builds/grafana_3.1.1-1470047149_amd64.deb
&& \  
dpkg -i grafana_3.1.1-1470047149_amd64.deb && \  
echo "deb https://packagecloud.io/grafana/stable/debian/ wheezy main" >>
/etc/apt/sources.list && \  
curl https://packagecloud.io/gpg.key | sudo apt-key add - && \  
apt-get update && \  
apt-get -y install grafana  
  
# install Maven 3.0.5  
WORKDIR /opt  
RUN wget http://archive.apache.org/dist/maven/maven-3/3.0.5/binaries/apache-
maven-3.0.5-bin.tar.gz && \  
tar -xzvf apache-maven-3.0.5-bin.tar.gz && \  
rm apache-maven-3.0.5-bin.tar.gz  
  
WORKDIR /home/jcconf  
  
# add in the environment deploy script  
ADD env-deploy.sh ./  
RUN chown jcconf:jcconf env-deploy.sh  
  
USER jcconf  
  
# using directly downloaded binaries for Apache Flink deployment (v1.1.2)  
RUN wget
http://ftp.twaren.net/Unix/Web/apache/flink/flink-1.1.2/flink-1.1.2-bin-
hadoop1-scala_2.10.tgz && \  
tar -xvf flink-1.1.2-bin-hadoop1-scala_2.10.tgz && \  
mv flink-1.1.2 flink && \  
rm flink-1.1.2-bin-hadoop1-scala_2.10.tgz  
  
# using directly downloaded binaries for Apache Kafka deployment (v0.9.0.1)  
RUN wget http://apache.stu.edu.tw/kafka/0.9.0.1/kafka_2.11-0.9.0.1.tgz && \  
tar -xvf kafka_2.11-0.9.0.1.tgz && \  
mv kafka_2.11-0.9.0.1 kafka && \  
rm kafka_2.11-0.9.0.1.tgz  
  
# will be using the workshop git repo to mirror code changes  
RUN git clone https://github.com/flink-taiwan/jcconf2016-workshop.git  
  
# set up env vars for Java and Maven paths  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> .bashrc && \  
echo "export PATH=/opt/apache-maven-3.0.5/bin:$PATH" >> .bashrc

