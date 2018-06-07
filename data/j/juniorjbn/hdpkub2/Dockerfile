FROM centos:centos6  
LABEL version="1.8.0"  
  
ENV TERM xterm  
  
# Any file with the "repo" extension will be added to /etc/yum.repos.d folder  
COPY *.repo /etc/yum.repos.d/  
  
RUN yum update -y -x kernel && \  
yum install -y \  
epel-release && \  
yum install -y \  
bind-utils \  
curl \  
git \  
krb5-libs \  
krb5-workstation \  
mc \  
mysql-connector-java \  
net-tools \  
ntp \  
openldap-clients \  
openssh-server \  
openssh-clients \  
sudo \  
tar \  
unzip \  
vim \  
wget \  
words  
  
RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/UTC /etc/localtime  
  
RUN sed -i 's/Defaults.*requiretty.*$/#Defaults requiretty/' /etc/sudoers  
  
# fix annoying PAM error 'couldnt open session'  
RUN sed -i "/pam_limits/ s/^/#/" /etc/pam.d/*  
  
RUN yum install -y ambari-server ambari-agent  
RUN ambari-server setup --silent  
  
# increase PermGen Space for Ambari views  
ENV AMBARI_JVM_ARGS -XX:MaxPermSize=512m  
  
# fixing pgsql issue  
RUN rm -rf /tmp/.s.PGSQL.5432.*  
  
COPY ["*.json", "start.sh", "/"]  
RUN chmod 755 /start.sh  
  
EXPOSE 8080  
VOLUME /var/log  
CMD ["/start.sh"]  

