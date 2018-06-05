FROM centos:latest  
MAINTAINER dayreiner  
  
# Using Veraticus cronsul fork. Does not require cronsul-cleanup, more robust.  
ENV
CRONSUL_URL=https://raw.githubusercontent.com/Veraticus/cronsul/master/cronsul
\  
PATH=/usr/local/bin:$PATH  
  
# Updates and install cronie  
RUN yum clean all && yum makecache fast && yum -y update  
RUN yum -y install epel-release && yum clean all && yum makecache fast && yum
-y update \  
&& yum -y install cronie git wget && yum clean all  
  
# Install Docker client so we can mount the local socket to run docker exec
jobs  
RUN curl -fsSL https://get.docker.com/ | sh  
  
# Move default cron-jobs file in to place. Should be overridden with local
volume  
COPY config/cron-jobs /cron-jobs  
COPY scripts/start.sh /start.sh  
  
# Install Veraticus cronsul fork  
# Fix PAM so cronsul can run outside systemd  
# per https://bugzilla.redhat.com/show_bug.cgi?id=1012420  
RUN wget -nv ${CRONSUL_URL} -O /usr/local/bin/cronsul \  
&& chmod 755 /usr/local/bin/cronsul \  
&& sed -i '/session required pam_loginuid.so/d' /etc/pam.d/crond  
  
CMD /start.sh  

