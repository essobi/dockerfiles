FROM seeruk/java:openjdk-java8  
MAINTAINER Elliot Wright <hello@elliotdwright.com>  
  
COPY provisioning/docker-entrypoint.sh /opt/sbt-setup/docker-entrypoint.sh  
  
ENV GOSU_VERSION 1.9  
ENV SBT_UID 1000  
ENV SBT_GID 1000  
ENV SBT_HOME /home/sbt  
ENV SBT_WORKDIR /app  
ENV SBT_VERSION 0.13.12  
ENV PATH ${PATH}:/usr/local/sbt/bin  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
git-core \  
language-pack-en-base \  
openssh-client \  
software-properties-common \  
wget \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/app/lists/* \  
&& curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local \  
&& echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built \  
&& chmod +x /opt/sbt-setup/docker-entrypoint.sh  
  
WORKDIR /opt/sbt-setup  
  
ENTRYPOINT ["/opt/sbt-setup/docker-entrypoint.sh"]  
  
CMD ["sbt", "sbtVersion"]  

