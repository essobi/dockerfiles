##############################  
# Alfred Centos 7 Base  
# Tag: kanalfred/centos7  
#  
# Refer:  
# https://bitbucket.org/cwt/docker-
centos7-ssh/src/9bbdf3fa4aca5d4c59eda4c28cfd231d951ffcc6/Dockerfile?fileviewer=file-
view-default  
# supervisord: https://serversforhackers.com/monitoring-processes-with-
supervisord  
# SSHD setup: https://github.com/tutumcloud/tutum-
centos/blob/master/centos7/Dockerfile  
# supervisord tutorial : https://serversforhackers.com/monitoring-processes-
with-supervisord  
# supervisord: https://hub.docker.com/r/jkuetemeier/docker-centos-supervisor-
cron/~/dockerfile/  
# supervisord: https://gist.github.com/Mulkave/10559775  
# supervisord: https://github.com/million12/docker-centos-supervisor  
#  
# Run:  
# docker run -h centos7 -p 192.168.3.129:22:22 -d --name centos7 -v
/home/alfred/docker/data/centos7:/home/alfred/doc kanalfred/centos7  
# docker run -e 'ROOT_PASSWORD=test123' -h centos7 --name centos7 -p 2201:22
-d kanalfred/centos7  
#  
# Build:  
# docker build -t kanalfred/centos7 .  
#  
# Dependancy:  
# Centos 7  
# DOCKERIZE_VERSION v0.2.0  
#  
# Permission:  
# etc drwxr-xr-x (755)  
# root dr-xr-x--- (550)  
##############################  
  
FROM centos:7  
MAINTAINER Alfred Kan <kanalfred@gmail.com>  
  
# Add Files  
#ADD container-files /  
# ssh key contain in root folder  
ADD container-files/root /root  
ADD container-files/etc /etc  
ADD container-files/config /config  
  
ENV DOCKERIZE_VERSION v0.2.0  
  
# root password  
#RUN echo 'root:xxxxx' | chpasswd  
#RUN cat /root/root.txt | chpasswd  
  
# Repo  
RUN yum -y install epel-release && yum clean all  
  
RUN \  
yum -y install \  
openssh openssh-server openssh-clients \  
sudo \  
passwd \  
cronie \  
wget \  
perl \  
mysql \  
rsync \  
rsnapshot \  
python-setuptools \  
sendmail \  
net-tools && \  
yum clean all && \  
  
# use easy install to get newer vesion of supervisor  
easy_install supervisor && \  
  
# ssh key file permission  
chmod 700 /root/.ssh && \  
chmod 600 /root/.ssh/authorized_keys && \  
  
# sshd  
sshd-keygen && \  
sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \  
  
# Set timezone (Pacific Time Zone) Vancouver  
rm -f /etc/localtime && \  
ln -s /usr/share/zoneinfo/Canada/Pacific /etc/localtime && \  
  
#RUN chmod 600 /etc/supervisord.conf /etc/supervisord.d/*.ini  
  
# Dockerize  
# Install dockerize - replace env var in config file  
wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Clean YUM caches to minimise Docker image size  
RUN yum clean all && rm -rf /tmp/yum*  
  
# Remove pass file  
#RUN rm -f /root/root.txt  
  
# EXPOSE  
EXPOSE 22  
  
# Run supervisord as demon with option -n  
CMD dockerize /config/run.sh  
#CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  
  

