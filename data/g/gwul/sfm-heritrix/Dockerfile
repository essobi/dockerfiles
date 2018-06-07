FROM
java@sha256:ea18d1cf75d819b8e1b2b9907d671703b8139598829492c315b0305205a2d0f1  
#openjdk-7  
MAINTAINER Justin Littman <justinlittman@gwu.edu>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.10  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
ENV lbs_version LBS-2016-02  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y \  
zip=3.0-8 && \  
apt-get install -y -t jessie-backports maven=3.3.*  
WORKDIR /tmp  
ADD https://github.com/Landsbokasafn/heritrix3/archive/${lbs_version}.zip
/tmp/  
RUN unzip ${lbs_version}.zip  
WORKDIR /tmp/heritrix3-${lbs_version}  
RUN mvn package -Dmaven.test.skip=true  
RUN unzip dist/target/heritrix-3.3.0-${lbs_version}-dist.zip -d /tmp  
RUN mv /tmp/heritrix-3.3.0-${lbs_version} /tmp/heritrix  
ADD start.sh /usr/local/bin/heritrix_start.sh  
RUN chmod +x /usr/local/bin/heritrix_start.sh  
  
EXPOSE 8443  
ENV FOREGROUND true  
CMD /usr/local/bin/heritrix_start.sh

