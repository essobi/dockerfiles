FROM ubuntu:14.04  
MAINTAINER Vjekoslav Nikolic <vnikolic@gmail.com>  
  
# Setup the key for Puppet PPA and add repo  
ADD image/puppetlabs-release-trusty.deb /tmp/puppetlabs-release-trusty.deb  
RUN dpkg -i /tmp/puppetlabs-release-trusty.deb && \  
sh -c 'echo "deb http://apt.puppetlabs.com// trusty main" >>
/etc/apt/sources.list.d/puppet.list'  
  
RUN apt-get update && apt-get install -y \  
openssh-server \  
supervisor \  
sudo \  
rsyslog \  
puppet  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/run/sshd && \  
mkdir -p /var/log/supervisor  
  
# Create user  
ENV USERNAME vagrant  
RUN useradd --create-home -s /bin/bash $USERNAME  
  
# Configure user - SSH access  
RUN mkdir -p /home/$USERNAME/.ssh && \  
echo "ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ==
$USERNAME insecure public key" > /home/$USERNAME/.ssh/authorized_keys && \  
chmod 700 /home/$USERNAME/.ssh && \  
echo -n "$USERNAME:$USERNAME" | chpasswd && \  
touch /home/$USERNAME/.hushlogin && \  
chown -R $USERNAME:$USERNAME /home/$USERNAME/ && \  
mkdir -p /etc/sudoers.d && echo "$USERNAME ALL= NOPASSWD: ALL" >
/etc/sudoers.d/$USERNAME && chmod 0440 /etc/sudoers.d/$USERNAME  
  
ADD image/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD image/entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
EXPOSE 22  
CMD ["/usr/local/bin/entrypoint.sh"]  

