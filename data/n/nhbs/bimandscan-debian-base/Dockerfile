#  
# 2018 © Headcount Solutions Ltd.  
# See 'LICENCE.md' in the project root for more information.  
#  
FROM debian:buster-slim  
MAINTAINER Neil Hyland <neil.hyland@bimandscan.com>  
  
# Install runtime libraries:  
RUN mkdir -p "/tmp"  
COPY ./DockerBuild.sh /tmp/DockerBuild.sh  
RUN chmod +x "/tmp/DockerBuild.sh"  
RUN bash -c "/tmp/DockerBuild.sh"  
  

