FROM million12/nginx-php:latest  
MAINTAINER Marcin Ryzycki marcin@m12.io  
  
# - Install OpenSSH server  
# - Generate required host keys  
# - Remove 'Defaults secure_path' from /etc/sudoers which overrides path when
using 'sudo' command  
# - Add 'www' user to sudoers  
# - Remove non-necessary Supervisord services from parent image
'million12/nginx-php'  
# - Remove warning about missing locale while logging in via ssh  
RUN \  
yum install -y openssh-server pwgen sudo hostname vim mc links screen && \  
yum clean all && \  
  
wget -O unrar.rpm
http://pkgs.repoforge.org/unrar/unrar-5.0.3-1.el7.rf.x86_64.rpm && \  
rpm -ivh unrar.rpm && \  
  
ssh-keygen -q -b 1024 -N '' -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -b 1024 -N '' -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -b 521 -N '' -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key && \  
  
sed -i -r 's/.?UseDNS\syes/UseDNS no/' /etc/ssh/sshd_config && \  
sed -i -r 's/.?PasswordAuthentication.+/PasswordAuthentication no/'
/etc/ssh/sshd_config && \  
sed -i -r 's/.?UsePAM.+/UsePAM no/' /etc/ssh/sshd_config && \  
sed -i -r
's/.?ChallengeResponseAuthentication.+/ChallengeResponseAuthentication no/'
/etc/ssh/sshd_config && \  
sed -i -r 's/.?PermitRootLogin.+/PermitRootLogin no/' /etc/ssh/sshd_config &&
\  
  
sed -i '/secure_path/d' /etc/sudoers && \  
echo 'www ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/www && \  
  
rm -rf /config/init/10-nginx-data-dirs.sh /etc/supervisor.d/nginx.conf
/etc/supervisor.d/php-fpm.conf && \  
echo > /etc/sysconfig/i18n  
  
# Add config/init scripts to run after container has been started  
ADD container-files /  
  
EXPOSE 22  
# Run container with following ENV variable to add listed users' keys from
GitHub.  
# Note: separate with coma, space is not allowed here!  
#ENV IMPORT_GITHUB_PUB_KEYS github,usernames,coma,separated  

