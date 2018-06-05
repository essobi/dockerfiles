FROM python:2.7.9  
MAINTAINER Tom Jackson thomas.jackson@nordstrom.com  
  
# define env variables that will allow all provisioners to navigate the  
# outbound proxy  
# ENV http_proxy http://pbcld-proxy.nordstrom.net:3128  
# ENV https_proxy https://pbcld-proxy.nordstrom.net:3128  
# ENV no_proxy localhost,10.0.0/8,nordstrom.net  
# define install dir  
ENV BACKUP_INSTALL /usr/local/backups  
  
# define logging dir  
ENV BACKUP_HOME /var/local/backups  
  
# install web for readme server  
RUN easy_install web.py  
  
# install required python modules  
RUN pip install awscli  
RUN pip install schedule  
RUN pip install boto  
  
# Install VIM so we have at least some editing capability inside container  
RUN apt-get update --quiet  
RUN printf 'Y' | apt-get install vim  
  
# Create home directory  
RUN mkdir -p "${BACKUP_HOME}"  
  
# Add scripts and config file to backup-install directory  
ADD src/ ${BACKUP_INSTALL}/src/  
ADD lib/ ${BACKUP_INSTALL}/lib/  
ADD config/ ${BACKUP_INSTALL}/config/  
  
# Add boto config file to control timeouts  
ADD config/boto.cfg /etc/boto.cfg  
  
# Run under the root account, since host directories containing logs may or
may not  
# be accessible to non-root users.  
# Set the working directory to the backup-install directory  
WORKDIR ${BACKUP_INSTALL}  
  
# Container hostname - used to tag each logs message to make it easier to
deconcolve log messages  
# in log aggregators (like cloud watch logs) coming from multiple lower
environments and/or clustered app tiers  
ENV HOSTNAME myhost-env  
# The CONFIGS_PATH variable defines the S3 URL for the backup configs file
that defines what needs to get backed up  
# The variable must be provided when the container is started, otherwise the
container will log an error message and  
# exit.  
# See REAME for details on how to specify the path.  
# launch the backup service in foreground  
CMD python -m src.backup $CONFIGS_PATH $HOSTNAME  

