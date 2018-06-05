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
&& apt-get purge -y --auto-remove curl  
  
# # grab the bamboo dependencies  
RUN apt-get update && apt-get install -y ca-certificates \  
&& echo "deb http://http.debian.net/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update && apt-get install -y \  
openjdk-8-jdk \  
libtcnative-1 \  
git \  
subversion \  
mercurial \  
cvs \  
docker.io \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /ect/apt/sources.list.d/jessie-backports.list  
  
ENV BAMBOO_VERSION 5.10.3  
ENV BAMBOO_HOME /var/atlassian/bamboo  
  
# extract bamboo  
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /opt/atlassian \  
&& curl -o /opt/atlassian/atlassian-bamboo.tar.gz -SL
'https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-5.10.3.tar.gz' \  
&& tar xf /opt/atlassian/atlassian-bamboo.tar.gz -C /opt/atlassian --strip-
components=1 \  
&& echo "bamboo.home=$BAMBOO_HOME" > /opt/atlassian/atlassian-bamboo/WEB-
INF/classes/bamboo-init.properties \  
&& rm -f /opt/atlassian/atlassian-bamboo.tar.gz \  
&& chown -R atlassian /opt/atlassian \  
&& apt-get purge -y --auto-remove curl  
  
VOLUME /var/atlassian/bamboo  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# http(s), remote agent  
EXPOSE 8085 54663  
CMD ["bamboo"]

