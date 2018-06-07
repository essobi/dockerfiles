FROM centos:6  
## Install dependencies ##  
COPY Tuleap.repo /etc/yum.repos.d/Tuleap.repo  
  
RUN useradd --home /var/lib/gitolite --create-home gitolite && \  
yum install -y epel-release && \  
yum install -y python-grokmirror \  
git19-git \  
openssh-server \  
gitolite3 \  
php-cli \  
tuleap-gitolite-membership-0.3 && \  
yum clean all && \  
service sshd start  
  
# Setup gitolite  
COPY gitolite.rc /root/.gitolite.rc  
  
# Setup tuleap-gitolite-membership  
COPY tuleap-gitolite-membership.ini /etc/tuleap-gitolite-membership.ini  
  
# Grokmirror  
COPY repos.conf /etc/grokmirror/repos.conf  
  
# Fix all ownership  
RUN mkdir /var/log/grokmirror /var/lock/grokmirror && \  
chown -R gitolite:gitolite /etc/tuleap-gitolite-membership.ini /etc/grokmirror
/var/log/grokmirror /var/lock/grokmirror  
  
COPY update_gladmin.sh /usr/local/bin/update_gladmin.sh  
COPY run.sh /run.sh  
COPY start_grokpull.sh /start_grokpull.sh  
  
VOLUME [ "/var/lib/gitolite" ]  
  
ENTRYPOINT [ "/run.sh" ]  

