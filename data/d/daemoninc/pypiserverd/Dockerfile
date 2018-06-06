FROM ubuntu:16.04  
MAINTAINER "Rsrp Sinr" <rsrp.sinr@gmail.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
locales \  
&& rm -rf /var/lib/apt/lists/*  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
#---------------------------------------------  
# PyPiServerD  
#---------------------------------------------  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
vim \  
curl \  
ssh \  
tar \  
unzip \  
build-essential \  
jq \  
wget \  
iputils-ping \  
krb5-user \  
ldap-utils \  
expect \  
software-properties-common \  
libnss-ldap \  
libpam-ldap \  
ldap-utils \  
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
DEBIAN_FRONTEND=noninteractive apt-get install -y libpcap-dev && \  
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
  
# Python  
# Ubuntu 16.04 image now defaults to Python3.5  
#---------------------------------------------  
RUN yes | add-apt-repository ppa:deadsnakes/ppa && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python3.4 \  
python2.7 \  
python-dev && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /usr/bin/python && \  
ln -s /usr/bin/python3.4 /usr/bin/python && \  
wget -qO - https://bootstrap.pypa.io/get-pip.py | /usr/bin/python2.7 && \  
rm -f /usr/local/bin/pip && \  
wget -qO - https://bootstrap.pypa.io/get-pip.py | /usr/bin/python3.4  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apache2 &&\  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install passlib && \  
pip install pypiserver  
  
EXPOSE 80  
VOLUME ["/pypi"]  
  
ENV PYPISERVERD_VERSION 0.3  
  
ADD app.sh /app.sh  
RUN chmod 700 /app.sh  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]

