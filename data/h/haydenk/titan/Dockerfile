FROM debian:jessie  
  
MAINTAINER Hayden King <hayden.king@gmail.com>  
  
ENV TITAN_VERSION="1.0.0"  
ENV TITAN_DEPLOYMENT="titan-$TITAN_VERSION-hadoop1"  
# Install dependencies and  
# make sure OpenJDK is not present  
RUN apt-get purge -y openjdk* && \  
apt-get update && \  
apt-get install -y \  
software-properties-common \  
python-software-properties \  
openssh-server \  
curl \  
unzip  
  
# Install Oracle Java 8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer oracle-java8-set-default  
  
# Setup ssh key  
RUN sed -i 's/required[ ]*pam_loginuid/optional\tpam_loginuid/g'
/etc/pam.d/sshd \  
&& mkdir -p /var/run/sshd \  
&& echo "UserKnownHostsFile /dev/null\nStrictHostKeyChecking no\nLogLevel
quiet" >> /etc/ssh/ssh_config \  
&& ssh-keygen -t dsa -P '' -f /root/.ssh/id_dsa \  
&& cat /root/.ssh/id_dsa.pub >> /root/.ssh/authorized_keys \  
&& chmod 600 /root/.ssh/id_dsa /root/.ssh/authorized_keys \  
&& chmod 644 /root/.ssh/id_dsa.pub  
  
# Download Titan  
RUN cd /opt && \  
curl -L -o titan-hadoop.zip
http://s3.thinkaurelius.com/downloads/titan/$TITAN_DEPLOYMENT.zip && \  
unzip /opt/titan-hadoop.zip && rm -vf /opt/titan-hadoop.zip && \  
ln -vsf /opt/$TITAN_DEPLOYMENT /opt/titan  
  
COPY gremlin-server.yaml /opt/titan/conf/gremlin-server/gremlin-server.yaml  
COPY titan-cassandra-es.properties /opt/titan/conf/gremlin-server/titan-
cassandra-es-server.properties  
  
COPY run-titan.sh /run-titan.sh  
RUN chmod -v +x /run-titan.sh  
  
EXPOSE 8182  
EXPOSE 8184  
WORKDIR /opt/titan  
  
CMD ["/run-titan.sh"]  

