FROM ubuntu:16.04  
MAINTAINER "Rsrp Sinr" <rsrp.sinr@gmail.com>  
  
#---------------------------------------------  
# TimelineD  
#---------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
locales \  
&& rm -rf /var/lib/apt/lists/*  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
vim \  
curl \  
ssh \  
tar \  
unzip \  
software-properties-common \  
build-essential \  
jq \  
wget \  
iputils-ping \  
netcat \  
libreadline-gplv2-dev \  
libncursesw5-dev \  
libssl-dev \  
libsqlite3-dev \  
tk-dev \  
libgdbm-dev \  
libc6-dev \  
libbz2-dev \  
expect \  
libnss-ldap \  
libpam-ldap \  
ldap-utils \  
krb5-user \  
libsnappy1v5 \  
libsnappy-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
#==============================================  
# Oracle JDK 1.8 installation  
#-----------------------------------------------------  
# Install Oracle JDK 1.8 (ver jdk1.8.0_111)  
#-----------------------------------------------------  
RUN mkdir -p /usr/java && \  
wget -qO -
https://www.dropbox.com/s/1eee6lcq87zub3b/jdk-8u111-linux-x64.tar.gz | tar xz
-C /usr/java && \  
ln -s /usr/java/jdk1.8.0_111 /usr/java/default  
ENV JAVA_HOME /usr/java/default  
ENV PATH $JAVA_HOME/bin:$PATH  
  
#-----------------------------------------------------  
# Install JCE for Oracle JDK 1.8  
#-----------------------------------------------------  
RUN wget -qO /tmp/jce_policy-8.zip
https://www.dropbox.com/s/s60yk9wt9sb3l75/jce_policy-8.zip && \  
unzip -o -j -q /tmp/jce_policy-8.zip -d $JAVA_HOME/jre/lib/security/ && \  
rm -f /tmp/jce_policy-8.zip  
  
#----------------------------------------------------------  
# JSVC setup  
#----------------------------------------------------------  
RUN apt-get update && \  
apt-get install -y libpcap-dev && \  
rm -rf /var/lib/apt/lists/* && \  
wget -qO /tmp/temp.zip https://www.dropbox.com/s/z1a8rxfv47l34bo/commons-
daemon-1.0.15-src.zip && \  
unzip /tmp/temp.zip -d /tmp/commons-daemon-1.0.15-src && \  
rm -f /tmp/temp.zip && \  
cd /tmp/commons-daemon-1.0.15-src/commons-daemon-1.0.15-src/src/native/unix &&
\  
./configure --with-java=/usr/java/default && \  
make && \  
mkdir -p /usr/hdp/current/bigtop-utils && \  
mv ./jsvc /usr/hdp/current/bigtop-utils && \  
rm -rf /tmp/commons-daemon-1.0.15-src  
WORKDIR /  
RUN rm -rf /tmp/commons-daemon-1.0.15-src  
  
#==============================================  
# Perl  
#---------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libxml2-dev \  
zlibc \  
zlib1g \  
zlib1g-dev &&\  
rm -rf /var/lib/apt/lists/* && \  
curl -L http://cpanmin.us | perl - App::cpanminus && \  
cpanm Fatal && \  
cpanm XML::LibXML && \  
cpanm JSON && \  
cpanm JSON::Parse  
ADD xml_edit.pl /usr/bin/xml_edit.pl  
RUN chmod a+x /usr/bin/xml_edit.pl  
  
# Python  
# Ubuntu 16.04 image now defaults to Python3.5  
#---------------------------------------------  
RUN yes | add-apt-repository ppa:deadsnakes/ppa && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python2.7 \  
python-dev && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /usr/bin/python && \  
ln -s /usr/bin/python3.5 /usr/bin/python && \  
wget -qO - https://bootstrap.pypa.io/get-pip.py | /usr/bin/python2.7 && \  
rm -f /usr/local/bin/pip && \  
wget -qO - https://bootstrap.pypa.io/get-pip.py | /usr/bin/python3.5  
  
# Apache Hadoop 2.7.6  
#---------------------------------------------  
RUN wget -qO -
https://dist.apache.org/repos/dist/release/hadoop/common/hadoop-2.7.6/hadoop-2.7.6.tar.gz
| tar xz -C /tmp && \  
mv /tmp/hadoop-2.7.6 /usr/local/hadoop && \  
mkdir -p /etc/hadoop/conf  
ENV HADOOP_CONF_DIR "/etc/hadoop/conf"  
ENV PATH "$PATH:/usr/local/hadoop/bin:/etc/hadoop/conf"  
ENV HADOOP_HOME "/usr/local/hadoop"  
ENV LD_LIBRARY_PATH "$HADOOP_HOME/lib/native"  
# Ensure root ownership of /usr/local/hadoop  
#----------------------------------------------  
RUN chown -R root:root /usr/local/hadoop  
  
# Install Spark 2.3.0  
#----------------------------------------------  
RUN wget -qO - http://www-
us.apache.org/dist/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz | tar xz -C
/tmp && \  
mv /tmp/spark-2.3.0-bin-hadoop2.7 /usr/local/spark && \  
chown -R root:root /usr/local/spark  
ENV PATH "$PATH:/usr/local/spark/bin"  
ENV SPARK_HOME "/usr/local/spark"  
ENV SPARK_CONF_DIR "/etc/spark/conf"  
ENV HADOOP_HOME "/usr/local/hadoop"  
# Some links required between Hadoop and Spark  
#---------------------------------------------  
RUN ln -s /usr/local/spark/yarn/spark-2.3.0-yarn-shuffle.jar
/usr/local/hadoop/share/hadoop/yarn/spark-2.3.0-yarn-shuffle.jar  
  
# Additional perl modules  
#---------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libssh2-1-dev \  
&& rm -rf /var/lib/apt/lists/*  
RUN cpanm XML::Simple && \  
cpanm Net::SSH2  
  
ENV TIMELINED_VERSION 0.5  
ADD app.sh /app.sh  
RUN chmod +x /app.sh  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

