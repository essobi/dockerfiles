# Leadware  
#  
# Gitlab CE Server Dockerfile  
# https://bitbucket.org/leadware/dockerfile-gitlab-ce  
# https://jetune@bitbucket.org/leadware/dockerfile-gitlab-ce.git  
# git@bitbucket.org:leadware/dockerfile-gitlab-ce.git  
#  
# Pull base image.  
FROM gitlab/gitlab-ce:10.1.4-ce.0  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# LW_DATA_HOME  
ARG LW_DATA_HOME=/var/leadware/gitlab  
  
# Install necessary for mysql  
RUN apt-get update && apt-get install -y libmysqlclient-dev gcc make  
  
# Add Entry point script file  
ADD entrypoint.sh /leadware-entrypoint.sh  
  
# Give wright to all sh file  
RUN \  
  
# Set right  
chmod 755 /leadware-entrypoint.sh  
  
# Command  
CMD ["/leadware-entrypoint.sh"]

