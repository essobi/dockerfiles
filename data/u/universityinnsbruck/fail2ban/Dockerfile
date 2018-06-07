FROM phusion/baseimage:latest  
MAINTAINER Gregor Schwab <gregor.schwab@uibk.ac.at>  
  
# Regenerate SSH host keys and allow ssh.  
RUN rm -f /etc/service/sshd/down  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Set Timezone  
RUN echo "Europe/Berlin" | tee /etc/timezone  
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Berlin
/etc/localtime  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
# Update Package List  
RUN apt-get update  
  
# Installing the 'apt-utils' package gets rid of the 'debconf: delaying
package configuration, since apt-utils is not installed'  
# error message when installing any other package with the apt-get package
manager.  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
apt-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Some PPAs  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y vim
curl wget build-essential software-properties-common git sudo iptables  
  
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install debian-keyring  
  
#----------  
# Fail2Ban  
#----------  
#get the newest Fail2ban server that allows foreground mode (no daemon)  
# SEE https://github.com/fail2ban/fail2ban/issues/1139  
RUN git clone https://github.com/fail2ban/fail2ban.git  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-downgrades
--allow-remove-essential --allow-change-held-packages python python-pyinotify
gamin libgamin-dev python-dnspython python-systemd  
RUN cd fail2ban && python setup.py install  
#add any additional config jails/filters here or mount as volume  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/fail2ban.log  
  
#------------------------------  
# Custom Scripts  
#------------------------------  
RUN mkdir /opt/build-scripts  
RUN chmod +x /opt/build-scripts  
COPY build/config.sh /opt/build-scripts/config.sh  
  
#------------------------------  
# Startup Scripts  
#------------------------------  
# create script directory  
RUN mkdir -p /etc/my_init.d  
  
# add scripts  
ADD build/envars.sh /etc/my_init.d/01_envars.sh  
  
# update script permissions  
RUN chmod +x /etc/my_init.d/*  
  
#start fail2ban in foreground mode  
#RUN echo "-f" > /etc/container_environment/FAIL2BAN_OPTS  
RUN mkdir /etc/service/fail2ban  
ADD build/fail2ban/fail2ban.sh /etc/service/fail2ban/run  
RUN chmod +x /etc/service/fail2ban/run  
  
#needed for fail2ban ssh  
RUN touch /var/log/auth.log  
  
#------------------------------  
# Finish and Cleanup  
#------------------------------  
EXPOSE 22  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

