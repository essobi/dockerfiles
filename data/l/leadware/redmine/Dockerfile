# Leadware  
#  
# Redmine Server Dockerfile  
# https://bitbucket.org/leadware/dockerfile-redmine  
# https://jetune@bitbucket.org/leadware/dockerfile-redmine.git  
# git@bitbucket.org:leadware/dockerfile-redmine.git  
#  
# Pull base image.  
FROM redmine:3.4.3  
  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# Redmine Home Argument  
ARG REDMINE_HOME=/usr/src/redmine  
  
# Set Environment REDMINE_HOME  
ENV REDMINE_HOME $REDMINE_HOME  
# Set Environment REDMINE_CONFIG_HOME  
ENV REDMINE_CONFIG_HOME $REDMINE_HOME/config  
  
# Set Environment REDMINE_PLUGINS_HOME  
ENV REDMINE_PLUGINS_HOME $REDMINE_HOME/plugins  
  
# Root User  
USER root  
  
# Run initializations.  
RUN apt-get update -y && \  
apt-get install -y unzip git  
  
# Add Entry point script file  
ADD entrypoint.sh /leadware-redmine-entrypoint.sh  
  
# Set execution right for any  
RUN chmod +x /leadware-redmine-entrypoint.sh  
  
# Set Entrypoint  
ENTRYPOINT ["/leadware-redmine-entrypoint.sh"]  
  
# Command  
CMD ["rails", "server", "-b", "0.0.0.0"]

