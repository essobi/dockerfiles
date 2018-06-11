##################################################  
#  
# Dockerfile for Postgresql  
#  
###################################################  
FROM unisis/base  
MAINTAINER Unisis <contacto@unisis.com.ar>  
  
VOLUME ["/var/lib/postgresql", "var/log/postgresql"]  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
# SSH server is installed because it's a BarMan requirement (even local)  
RUN apt-get update  
RUN apt-get -y install \  
postgresql \  
openssh-server  
  
# From http://stackoverflow.com/questions/18173889/cannot-access-centos-sshd-
on-docker  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
# Copy config files  
ENV CONF_REFRESHED_AT 2016_06_05  
ADD config/ssh_config /root/ssh_config  
ADD config/pg_hba.conf /root/pg_hba.conf  
ADD config/postgresql.conf /root/postgresql.conf  
  
# Copy start script  
ADD scripts/start.sh /root/start.sh  
RUN chmod +x /root/start.sh  
  
# Copy init script  
ADD scripts/init.sh /root/init.sh  
RUN chmod +x /root/init.sh  
  
# Run Init script  
CMD ["/root/start.sh"]  

