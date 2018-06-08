FROM sloppycoder/java-base  
MAINTAINER Li Lin <guru.lin@gmail..com>  
  
# Download and extract Bamboo  
ENV BAMBOO_VERSION 5.9.7  
RUN curl -Lks
http://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz \  
-o /root/bamboo.tar.gz \  
&& mkdir /opt/bamboo \  
&& tar zxf /root/bamboo.tar.gz \--strip=1 -C /opt/bamboo \  
&& rm /root/bamboo.tar.gz \  
&& sed -i -e "s/^#!\/bin\/sh/#!\/bin\/bash/" /opt/bamboo/bin/catalina.sh \  
&& mv /opt/bamboo/conf/server.xml /opt/bamboo/conf/server.xml.orig \  
&& echo "bamboo.home=/opt/atlassian-home/bamboo" > /opt/bamboo/atlassian-
bamboo/WEB-INF/classes/bamboo-init.properties  
  
# create group and users to run Stash  
RUN /usr/sbin/groupadd atlassian \  
&& /usr/sbin/useradd -M --home-dir /opt/bamboo \--groups atlassian --shell
/bin/bash bamboo \  
&& chown -R bamboo:bamboo /opt/bamboo  
  
ADD ./docker-entrypoint.sh /  
VOLUME ["/opt/atlassian-home"]  
  
ENV BAMBOO_HOME /opt/atlassian-home/bamboo  
ENV CONTEXT_PATH bamboo  
  
EXPOSE 8085 54663  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]  

