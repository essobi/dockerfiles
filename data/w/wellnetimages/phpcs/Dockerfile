FROM php:7.0.4  
RUN apt-get update && apt-get install -y openssh-server zip unzip curl  
  
# Install development tools  
ADD install-tools-for-code_sniffer.sh /tmp/install-tools-for-code_sniffer.sh  
RUN chmod a+x /tmp/install-tools-for-code_sniffer.sh  
RUN /tmp/install-tools-for-code_sniffer.sh && rm /tmp/install-tools-for-
code_sniffer.sh  
  
# Install xDebug  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
  
# Setup SSH.  
ADD install-ssh.sh /tmp/install-ssh.sh  
RUN chmod a+x /tmp/install-ssh.sh  
RUN /tmp/install-ssh.sh && rm /tmp/install-ssh.sh  
  
# Expose ssh access.  
EXPOSE 22  
# Change the UID and GID.  
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data  
  
# Run tests  
ADD test.sh /tmp/test.sh  
RUN chmod a+x /tmp/test.sh  
RUN /tmp/test.sh && rm /tmp/test.sh  
  
# Run container access.  
CMD ["/usr/sbin/sshd", "-D"]  

