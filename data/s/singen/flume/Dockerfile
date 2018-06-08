FROM centos:centos6  
LABEL version="1.3"  
  
ENV TERM=xterm \  
HDPVER=2.2.8.0 \  
FLUME_CONFDIR=/etc/flume/conf \  
JAVA_HOME=/usr/java/jdk1.7.0_79 \  
JAVA_JDK_DOWNLOAD_URL=http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz \  
JAVA_JCE_DOWNLOAD_URL=http://download.oracle.com/otn-
pub/java/jce/7/UnlimitedJCEPolicyJDK7.zip  
  
# RUN yum -y update -x kernel*; yum clean all  
RUN yum update -y -x kernel* && \  
yum install -y \  
epel-release && \  
yum install -y \  
bind-utils \  
chkconfig \  
coreutils \  
curl \  
# git \  
mc \  
net-tools \  
nfs-utils \  
ntp \  
# openssh-server \  
# openssh-clients \  
sudo \  
tar \  
unzip \  
vim \  
wget  
  
# Set time zone  
RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/UTC /etc/localtime  
  
# Install Java  
RUN wget -nv --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
${JAVA_JDK_DOWNLOAD_URL} -O /tmp/jdk-7-linux-x64.tar.gz && \  
wget -nv --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
${JAVA_JCE_DOWNLOAD_URL} -O /tmp/UnlimitedJCEPolicyJDK7.zip && \  
mkdir /usr/java && \  
tar xzvf /tmp/jdk-7-linux-x64.tar.gz -C /usr/java/ && \  
chown -R root:root /usr/java && \  
update-alternatives --verbose --install "/usr/bin/java" "java"
"${JAVA_HOME}/bin/java" 1 && \  
update-alternatives --verbose --install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1 && \  
update-alternatives --verbose --install "/usr/bin/javaws" "javaws"
"${JAVA_HOME}/bin/javaws" 1 && \  
update-alternatives --verbose --set java ${JAVA_HOME}/bin/java && \  
update-alternatives --verbose --set javac ${JAVA_HOME}/bin/javac && \  
update-alternatives --verbose --set javaws ${JAVA_HOME}/bin/javaws && \  
ln -vfs $JAVA_HOME /usr/java/default  
  
# Add HDP Repository  
RUN wget -nv -O /etc/yum.repos.d/hdp.repo http://public-
repo-1.hortonworks.com/HDP/centos6/2.x/updates/${HDPVER}/hdp.repo  
  
# Install Flume  
RUN yum install -y flume flume-agent  
  
# COPY ./lib/*jar /opt/flume/lib/  
#ENV PATH=/opt/apache-flume-${FLUME_VERSION}-bin/bin:$PATH  
## ENV
FLUME_CLASSPATH="/opt/flume/lib:/opt/hadoop/share/hadoop/common:/opt/hadoop/share/hadoop/common/lib"  
COPY ./configs/flume.conf ${FLUME_CONFDIR}/  
COPY ./configs/log4j.properties ${FLUME_CONFDIR}/  
  
# cannot create directory `/var/log/flume': File exists  
# RUN mkdir /var/log/flume  
VOLUME ["/data"]  
CMD [ "/usr/bin/flume-ng", "agent", "-n ", "a1", "-c", "/etc/flume/conf",
"-f", "/etc/flume/conf/flume.conf", "--name", "a1" ]  
# CMD [ "/usr/hdp/current/flume-server/bin/flume-ng", "agent", "-n ", "a1",
"-c", "${FLUME_CONFDIR}", "-f", "${FLUME_CONFDIR}/flume.conf", "--name", "a1"
]  

