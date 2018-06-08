# Creates pseudo distributed hadoop latest stable  
#  
# docker build -t p4km9y/hadoop .  
FROM java:openjdk-8  
MAINTAINER p4km9y  
  
#  
# https://github.com/sequenceiq/docker-pam  
#  
#Setup build environment for libpam  
#RUN apt-get -y build-dep pam  
#Rebuild and istall libpam with --disable-audit option  
#RUN export CONFIGURE_OPTS=--disable-audit && cd /root && apt-get -b source
pam && dpkg -i libpam-doc*.deb libpam-modules*.deb libpam-runtime*.deb
libpam0g*.deb  
# base updates & tools  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ADD ssh_config /root/.ssh/config  
RUN apt-get update -y && apt-get upgrade -y && \  
apt-get install -y curl wget tar sudo openssh-server openssh-client rsync && \  
rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key /root/.ssh/id_rsa &&
\  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa && \  
cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \  
chmod 600 /root/.ssh/config && \  
chown root:root /root/.ssh/config  
  
# https://hadoop.apache.org/docs/r2.7.2/hadoop-project-dist/hadoop-
common/ClusterSetup.html  
# hadoop installation  
ENV HADOOP_HOME /opt/hadoop  
ENV HADOOP_PREFIX /opt/hadoop  
ENV HADOOP_COMMON_HOME /opt/hadoop  
ENV HADOOP_HDFS_HOME /opt/hadoop  
ENV HADOOP_MAPRED_HOME /opt/hadoop  
ENV HADOOP_YARN_HOME /opt/hadoop  
ENV HADOOP_CONF_DIR /opt/hadoop/etc/hadoop  
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
ENV BOOTSTRAP /etc/bootstrap.sh  
  
ADD bootstrap.sh /etc/bootstrap.sh  
  
RUN current=http://www.apache.org/dist/hadoop/common/stable && \  
ref=$(wget -qO - ${current} | grep -v src\\\\. | grep -v doc | sed -n
's/.*href="\\(hadoop-.*\\.gz\\)".*/\1/p' | tail -1) && \  
wget -O - ${current}/${ref} | gzip -dc | tar x -C /opt/ -f - && \  
dir=`ls /opt | grep hadoop` && \  
ln -s /opt/${dir} ${HADOOP_HOME} && \  
sed -i '1iexport HADOOP_PREFIX=${HADOOP_PREFIX}\nexport
HADOOP_HOME=${HADOOP_HOME}' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \  
sed -i 's/^\\(export\s*JAVA_HOME\\)\s*=.*$/\1=\/usr\/lib\/jvm\/java-8-openjdk-
amd64/' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \  
mkdir $HADOOP_PREFIX/input && \  
cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input && \  
chown -R root:root ${HADOOP_HOME}/ && \  
chown root:root /etc/bootstrap.sh && \  
chmod 700 /etc/bootstrap.sh  
  
# hadoop configuration  
# pseudo distributed  
ADD core-site.xml.template $HADOOP_PREFIX/etc/hadoop/core-site.xml.template  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
  
RUN sed s/HOSTNAME/localhost/ $HADOOP_PREFIX/etc/hadoop/core-site.xml.template
> $HADOOP_PREFIX/etc/hadoop/core-site.xml && \  
$HADOOP_PREFIX/bin/hdfs namenode -format && \  
ls -la $HADOOP_PREFIX/etc/hadoop/*-env.sh && \  
chmod +x $HADOOP_PREFIX/etc/hadoop/*-env.sh && \  
ls -la $HADOOP_PREFIX/etc/hadoop/*-env.sh  
  
# fix the 254 error code  
RUN sed -i '/^[^#]*UsePAM/ s/.*/#&/' /etc/ssh/sshd_config && \  
echo "UsePAM no" >> /etc/ssh/sshd_config && \  
echo "Port 2122" >> /etc/ssh/sshd_config  
  
RUN service ssh start && \  
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \  
$HADOOP_PREFIX/sbin/start-dfs.sh && \  
$HADOOP_PREFIX/bin/hdfs dfs -mkdir -p /user/root && \  
$HADOOP_PREFIX/bin/hdfs dfs -put $HADOOP_PREFIX/etc/hadoop/ input  
  
VOLUME /opt/hadoop-config  
  
CMD ["/etc/bootstrap.sh", "-d"]  
  
# Hdfs ports  
EXPOSE 50010 50020 50070 50075 50090 8020 9000  
# Mapred ports  
EXPOSE 19888  
#Yarn ports  
EXPOSE 8030 8031 8032 8033 8040 8042 8088  
#Other ports  
EXPOSE 49707 2122  

