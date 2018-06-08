# Basics  
#  
# FROM durdn/atlassian-base  
# MAINTAINER Nicola Paolucci <npaolucci@atlassian.com>  
#FROM grahamrb/atlassian-base  
# switch back to using the official atlassian base as we haven't modified it  
FROM durdn/atlassian-base  
MAINTAINER Graham Rivers-Brown <graham@extg.net>  
  
# Install Bamboo  
ENV BAMBOO_VERSION 5.8.1  
RUN curl -Lks
http://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz -o /root/bamboo.tar.gz  
RUN /usr/sbin/useradd --create-home --home-dir /opt/bamboo --groups atlassian
--shell /bin/bash bamboo  
RUN tar zxf /root/bamboo.tar.gz --strip=1 -C /opt/bamboo  
RUN sed -i -e "s/^#!\/bin\/sh/#!\/bin\/bash/" /opt/bamboo/bin/catalina.sh  
RUN mv /opt/bamboo/conf/server.xml /opt/bamboo/conf/server-backup.xml  
RUN chown -R bamboo:bamboo /opt/bamboo  
  
ENV CONTEXT_PATH ROOT  
ADD launch.bash /launch  
  
# Launching Stash  
WORKDIR /opt/bamboo  
VOLUME /opt/atlassian-home  
EXPOSE 8085  
EXPOSE 54663  
USER bamboo  
CMD ["/launch"]  

