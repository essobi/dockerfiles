FROM centos:latest  
MAINTAINER Jacopo Labardi  
  
ADD script/run.sh /bin/run.sh  
  
RUN chmod +x /bin/run.sh && \  
rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7 && \  
rpm --import https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7 && \  
rpm --import https://dl.iuscommunity.org/pub/ius/IUS-COMMUNITY-GPG-KEY && \  
echo "exclude=postgresql*" >> "/etc/yum.repos.d/CentOS-Base.repo" && \  
yum update -y && \  
yum install -y
https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-
centos96-9.6-3.noarch.rpm && \  
yum install -y postgresql96-server \  
openssh \  
openssh-clients && \  
ln -s -f /usr/pgsql-9.6/bin/* /usr/bin/ && \  
cd /opt && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.tar.gz
\  
| tar -xzf - -C /opt && \  
ln -s /opt/jdk1.8.0_121 /opt/jdk &&\  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/lib/plugin.jar \  
/opt/jdk/jre/lib/ext/jfxrt.jar \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/lib/javaws.jar \  
/opt/jdk/jre/lib/desktop \  
/opt/jdk/jre/plugin \  
/opt/jdk/jre/lib/deploy* \  
/opt/jdk/jre/lib/*javafx* \  
/opt/jdk/jre/lib/*jfx* \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so && \  
alternatives --install /usr/bin/java java /opt/jdk1.8.0_121/bin/java 2 && \  
yum clean all && \  
mkdir /var/run/sshd && \  
su postgres -c "initdb -D /var/lib/pgsql/data -A trust --encoding=UTF8"  
  
ENV JAVA_HOME /opt/jdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
EXPOSE 5432  
  
CMD ["/bin/run.sh"]  
  

