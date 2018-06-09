# Basics  
#  
FROM mechatoni/trusty-java7  
MAINTAINER Toni Mecha <antonio.mecha@siqme.com>  
  
# Install Stash  
ENV STASH_VERSION 3.2.0  
RUN curl -Lks
http://www.atlassian.com/software/stash/downloads/binary/atlassian-
stash-${STASH_VERSION}.tar.gz -o /root/stash.tar.gz  
RUN /usr/sbin/useradd --create-home --home-dir /opt/stash --groups atlassian
--shell /bin/bash stash  
RUN tar zxf /root/stash.tar.gz --strip=1 -C /opt/stash  
RUN sed -i -e "s/^#!\/bin\/sh/#!\/bin\/bash/" /opt/stash/bin/catalina.sh  
RUN mv /opt/stash/conf/server.xml /opt/stash/conf/server-backup.xml  
RUN chown -R stash:stash /opt/atlassian-home  
RUN chown -R stash:stash /opt/stash  
  
ENV CONTEXT_PATH ROOT  
ENV STASH_HOME /opt/atlassian-home  
  
ADD launch.bash /launch  
  
# Launching Stash  
WORKDIR /opt/stash  
VOLUME /opt/atlassian-home  
EXPOSE 7990 7999  
USER stash  
  
CMD ["/launch"]  

