# Leadware  
#  
# Sonatype Nexus Server Dockerfile  
# https://bitbucket.org/leadware/dockerfile-nexus3  
# https://jetune@bitbucket.org/leadware/dockerfile-nexus3.git  
# git@bitbucket.org:leadware/dockerfile-nexus3.git  
#  
# Pull base image.  
FROM sonatype/nexus3:3.6.2  
  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# Sonatype home  
ARG SONATYPE_HOME=/opt/sonatype  
  
# Nexus Home  
ARG NEXUS_HOME=$SONATYPE_HOME/nexus  
  
# Nexus Home  
ARG NEXUS_DATA_HOME=/nexus-data  
  
# Nexus Data ETC Home  
ARG NEXUS_DATA_ETC_HOME="$NEXUS_DATA_HOME/etc"  
# Set ENV Sonatype Home  
ENV SONATYPE_HOME $SONATYPE_HOME  
# Set ENV Nexus Home  
ENV NEXUS_HOME $NEXUS_HOME  
# Set ENV Nexus Data Home  
ENV NEXUS_DATA_HOME $NEXUS_DATA_HOME  
# Set ENV Nexus Data etc Home  
ENV NEXUS_DATA_ETC_HOME $NEXUS_DATA_ETC_HOME  
# Set user to root  
USER root  
  
# Add Entry point script file  
ADD entrypoint.sh /leadware-entrypoint.sh  
  
# Give wright to all sh file  
RUN chmod 755 /leadware-entrypoint.sh  
  
# Command  
CMD ["/leadware-entrypoint.sh"]

