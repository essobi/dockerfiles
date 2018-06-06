FROM debian:jessie  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r atlassian && useradd -r -g atlassian atlassian  
  
# grab gosu for easy step-down from root  
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \  
&& gpg --keyserver pgp.mit.edu --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /tmp/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /tmp/gosu.asc /usr/local/bin/gosu \  
&& rm /tmp/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get purge -y \--auto-remove curl  
  
# grab the confluence dependencies  
RUN apt-get update && apt-get install -y ca-certificates \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >
/etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
>> /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886
\  
&& apt-get update && apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default \  
libtcnative-1 \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/oracle-jdk8-installer \  
&& rm -f /ect/apt/sources.list.d/webupd8team-java.list  
  
ENV CONFLUENCE_VERSION 5.10.8  
ENV CONFLUENCE_HOME /var/atlassian/confluence  
  
# extract confluence  
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /opt/atlassian \  
&& curl -o /opt/atlassian/atlassian-confluence.tar.gz -SL
'https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-5.10.8.tar.gz' \  
&& tar xf /opt/atlassian/atlassian-confluence.tar.gz -C /opt/atlassian
--strip-components=1 \  
&& echo "confluence.home=$CONFLUENCE_HOME" > /opt/atlassian/confluence/WEB-
INF/classes/confluence-init.properties \  
&& rm -f /opt/atlassian/atlassian-confluence.tar.gz \  
&& chown -R atlassian /opt/atlassian \  
&& apt-get purge -y \--auto-remove curl  
  
VOLUME /var/atlassian/confluence  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8090  
CMD ["confluence"]  

