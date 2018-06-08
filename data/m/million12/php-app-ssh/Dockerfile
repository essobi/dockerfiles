#  
# million12/php-app-ssh  
#  
FROM million12/nginx-php:latest  
MAINTAINER Marcin Ryzycki marcin@m12.io  
  
RUN \  
`# Install OpenSSH server` \  
yum install -y openssh-server pwgen sudo vim mc links && \  
yum clean all && \  
  
`# Configure SSH daemon...` \  
sed -i -r 's/.?UseDNS\syes/UseDNS no/' /etc/ssh/sshd_config && \  
sed -i -r 's/.?PasswordAuthentication.+/PasswordAuthentication no/'
/etc/ssh/sshd_config && \  
sed -i -r 's/.?UsePAM.+/UsePAM no/' /etc/ssh/sshd_config && \  
sed -i -r
's/.?ChallengeResponseAuthentication.+/ChallengeResponseAuthentication no/'
/etc/ssh/sshd_config && \  
sed -i -r 's/.?PermitRootLogin.+/PermitRootLogin no/' /etc/ssh/sshd_config &&
\  
  
`# Remove 'Defaults secure_path' from /etc/sudoers which overrides path when
using 'sudo' command` \  
sed -i '/secure_path/d' /etc/sudoers && \  
`# Add 'www' user to sudoers` \  
echo 'www ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/www && \  
  
`# Remove non-necessary files and Supervisord services from parent
million12/nginx-php image` \  
rm -rf /config/init/*-{nginx,php}-*.sh /etc/supervisor.d/{nginx,php-fpm}.conf
&& \  
  
`# Remove warning about missing locale while logging in via ssh` \  
echo > /etc/sysconfig/i18n  
  
# Add config/init scripts to run after container has been started  
ADD container-files /  
  
EXPOSE 22  
# Run container with following ENV variable to add listed users' keys from
GitHub.  
# Note: separate with coma, space is not allowed here!  
#ENV IMPORT_GITHUB_PUB_KEYS github,usernames,coma,separated  

