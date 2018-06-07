FROM php:5.6-fpm-alpine  
MAINTAINER Eugene Savchenko  
  
ENV PROJECT_PATH /var/www/  
ENV SSH_SERVER_KEYS /etc/ssh/host_keys/  
  
COPY /rootfs /  
  
#  
# Install ssh-server for connect remote php interpreter and supervisor  
#  
RUN apk update && \  
apk add bash openssh supervisor && \  
mkdir -p ${SSH_SERVER_KEYS} && \  
echo -e "HostKey ${SSH_SERVER_KEYS}ssh_host_rsa_key" >> /etc/ssh/sshd_config
&& \  
echo -e "HostKey ${SSH_SERVER_KEYS}ssh_host_dsa_key" >> /etc/ssh/sshd_config
&& \  
echo -e "HostKey ${SSH_SERVER_KEYS}ssh_host_ecdsa_key" >> /etc/ssh/sshd_config
&& \  
echo -e "HostKey ${SSH_SERVER_KEYS}ssh_host_ed25519_key" >>
/etc/ssh/sshd_config && \  
sed -i "s/#PermitRootLogin.*/PermitRootLogin\ yes/" /etc/ssh/sshd_config && \  
echo "root:root" | chpasswd && \  
chmod +x /usr/local/bin/entrypoint.sh && \  
rm -rf /var/cache/apk/* /tmp/*  
  
#  
# Saving ssh host keys  
#  
VOLUME ["${SSH_SERVER_KEYS}"]  
  
# php-fpm  
EXPOSE 9000  
# ssh  
EXPOSE 22  
WORKDIR ${PROJECT_PATH}  
  
ENTRYPOINT ["entrypoint.sh"]  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.d/supervisord.ini"]

