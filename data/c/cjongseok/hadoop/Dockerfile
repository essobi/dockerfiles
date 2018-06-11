from ubuntu:14.04  
ENV ORACLE_JDK_VERSION=1.8.0_77  
ENV HADOOP_VERSION=2.4.1  
# install dependencies  
RUN set -ex \  
&& apt-get update \  
&& apt-get -y install wget curl build-essential \  
&& apt-get -y install alien dpkg-dev debhelper \  
&& apt-get -y install dnsutils  
  
# install oracle jdk 8  
#RUN set -ex \  
# && apt-get -y install software-properties-common \  
# && apt-add-repository ppa:webupd8team/java \  
# && apt-get update \  
# && echo y | apt-get -y install oracle-java8-installer  
# install oracle jdk 8  
RUN set -ex \  
&& mkdir -p /usr/java \  
&& cd /usr/java \  
# && curl -LO --insecure --junk-session-cookies --location --remote-name
--silent --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u77-b03/jdk-8u77-linux-x64.rpm \  
&& curl -LO --insecure --junk-session-cookies --location --remote-name
--silent --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u77-b03/jdk-8u77-linux-x64.tar.gz
\  
&& tar xvzf jdk-8u77-linux-x64.tar.gz  
# && alien jdk-8u77-linux-x64.rpm \  
# && dpkg -i jdk1.8.0-77_1.8.077-1_amd64.deb  
#ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle  
ENV JAVA_HOME=/usr/java/jdk${ORACLE_JDK_VERSION}  
ENV HADOOP_PREFIX=/opt/hadoop-${HADOOP_VERSION}  
ENV HADOOP_HOME=${HADOOP_PREFIX}  
ENV HADOOP_YARN_HOME=${HADOOP_HOME}  
ENV PATH=${PATH}:${JAVA_HOME}/bin:${HADOOP_PREFIX}/bin  
  
RUN echo "export JAVA_HOME=${JAVA_HOME}" >> /etc/profile \  
&& echo "export HADOOP_PREFIX=${HADOOP_PREFIX}" >> /etc/profile \  
&& echo "export PATH=${PATH}" >> /etc/profile  
  
WORKDIR ${HADOOP_PREFIX}  
  
# install hadoop binary  
ENV HADOOP_CONF_DIR="${HADOOP_PREFIX}/conf"  
ENV HADOOP_NAMENODE_OPTS="-XX:+UseParallelGC ${HADOOP_NAMENODE_OPTS}"  
ENV HADOOP_LOG_DIR=${HADOOP_HOME}/logs  
RUN set -ex \  
&& cd /opt \  
&& wget
https://archive.apache.org/dist/hadoop/core/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
\  
# && wget
http://apache.mirror.cdnetworks.com/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
\  
&& tar xvzf hadoop-${HADOOP_VERSION}.tar.gz \  
&& sed -i '1iexport HADOOP_NAMENODE_OPTS='"${HADOOP_NAMENODE_OPTS}"''
${HADOOP_PREFIX}/libexec/hadoop-config.sh \  
&& sed -i '1iJAVA_HOME='"${JAVA_HOME}"'' ${HADOOP_PREFIX}/libexec/hadoop-
config.sh \  
# set up hadoop conf files  
&& mkdir -p ${HADOOP_CONF_DIR}  
COPY conf ${HADOOP_CONF_DIR}  
  
# configure hadoop  
COPY conf/*.xml ${HADOOP_PREFIX}/etc/hadoop/  
  
# set up ssh server and key  
ENV NOTVISIBLE "in users profile"  
RUN set -ex \  
&& apt-get -y install ssh openssh-server \  
&& ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa \  
&& cat /root/.ssh/id_dsa.pub >> /root/.ssh/authorized_keys \  
&& cat /root/.ssh/id_dsa.pub >> /root/.ssh/known_hosts \  
&& mkdir /var/run/sshd \  
&& echo 'root:screencast' | chpasswd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& echo "export VISIBLE=now" >> /etc/profile  
# && update-rc.d ssh defaults  
# && sed -i 's/^\\(exit.*\\)/service ssh start\n\1/g' /etc/rc.local  
# && service ssh start  
# run ssh at start-up  
COPY start /opt/start  
COPY tools.sh /opt/tools.sh  
COPY srv_resolver.sh /opt/srv_resolver.sh  
  
EXPOSE 22 9000 50070 50090 50010 50020 50075  
#CMD ["/opt/start"]  
#CMD ["/usr/sbin/sshd", "-D"]  
ENTRYPOINT ["/opt/start"]  
#ENTRYPOINT ["/bin/bash"]  

