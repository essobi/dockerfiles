FROM debian:jessie-backports  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r atlassian && useradd -r -g atlassian atlassian  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
# grab the bitbucket dependencies  
RUN apt-get update && apt-get install -y \  
openjdk-8-jre-headless \  
libtcnative-1 \  
git \  
perl \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV BITBUCKET_VERSION 4.8.1  
# extract bitbucket  
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /opt/atlassian \  
&& curl -s -o /opt/atlassian/atlassian-bitbucket.tar.gz -SL
'https://www.atlassian.com/software/stash/downloads/binary/atlassian-
bitbucket-4.8.1.tar.gz' \  
&& tar xf /opt/atlassian/atlassian-bitbucket.tar.gz -C /opt/atlassian --strip-
components=1 \  
&& rm -f /opt/atlassian/atlassian-bitbucket.tar.gz \  
&& mkdir -p /opt/atlassian/lib/native \  
&& ln -s /usr/lib/x86_64-linux-gnu/libtcnative-1* /opt/atlassian/lib/native \  
&& chown -R atlassian /opt/atlassian \  
&& apt-get purge -y --auto-remove curl  
  
ENV BITBUCKET_HOME /var/atlassian/bitbucket  
VOLUME /var/atlassian/bitbucket  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# http(s), ssh  
EXPOSE 7990 7999  
CMD ["bitbucket"]

