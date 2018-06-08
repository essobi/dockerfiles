FROM sloppycoder/java-base  
MAINTAINER Li Lin <guru.lin@gmail..com>  
  
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*  
  
# Download and extract Stash  
ENV STASH_VERSION 3.11.4  
RUN curl -Lks
http://www.atlassian.com/software/stash/downloads/binary/atlassian-
stash-${STASH_VERSION}.tar.gz \  
-o /root/stash.tar.gz \  
&& mkdir /opt/stash \  
&& tar zxf /root/stash.tar.gz --strip=1 -C /opt/stash \  
&& rm /root/stash.tar.gz \  
&& sed -i -e "s/^#!\/bin\/sh/#!\/bin\/bash/" /opt/stash/bin/catalina.sh \  
&& mv /opt/stash/conf/server.xml /opt/stash/conf/server.xml.orig  
  
# create group and users to run Stash  
RUN /usr/sbin/groupadd atlassian \  
&& /usr/sbin/useradd -M --home-dir /opt/stash --groups atlassian --shell
/bin/bash stash \  
&& chown -R stash:stash /opt/stash  
  
ADD ./docker-entrypoint.sh /  
VOLUME ["/opt/atlassian-home"]  
  
ENV STASH_HOME /opt/atlassian-home/stash  
ENV CONTEXT_PATH stash  
  
EXPOSE 7990 7999  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]  

