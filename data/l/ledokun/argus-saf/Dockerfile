FROM alpine:3.6  
MAINTAINER Rom Luengwattanapong <s1567783@ed.ac.uk>  
  
USER root  
  
# Installs bash and php for run script  
RUN apk --no-cache upgrade \  
&& apk --no-cache add \  
bash \  
coreutils \  
php7 \  
php7-posix \  
php7-json  
  
# Installs Dependencies  
RUN apk --no-cache add --virtual .build-dependencies \  
ca-certificates \  
curl \  
git \  
openssl \  
tar \  
unzip \  
wget  
  
# Installs OpenJDK-8  
RUN apk --no-cache add openjdk8-jre  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
  
# Installs Argus-SAF  
ENV ARGUS_URL
https://bintray.com/arguslab/maven/download_file?file_path=com%2Fgithub%2Farguslab%2Fargus-
saf_2.12%2F3.1.1%2Fargus-saf_2.12-3.1.1-assembly.jar  
ENV ARGUS_ROOT /opt/argus  
ENV PATH ${ARGUS_ROOT}:$PATH  
  
COPY dummy.apk /tmp  
  
RUN mkdir -p ${ARGUS_ROOT} \  
&& wget ${ARGUS_URL} -O ${ARGUS_ROOT}/argus-saf-assembly.jar \  
&& java -jar ${ARGUS_ROOT}/argus-saf-assembly.jar a /tmp/dummy.apk \  
&& rm -f /tmp/dummy.apk  
  
# Cleans up  
RUN apk del .build-dependencies \  
&& rm -rf /tmp/* /var/tmp/*  
  
# Setups run environment  
ENV _JAVA_OPTIONS -Djava.io.tmpdir=/var/tmp  
  
# Create application folder  
RUN mkdir -p /app  
  
VOLUME ["/app"]  
  
COPY run.php /tmp/  
RUN chmod +x /tmp/run.php  
WORKDIR /tmp  
  
ENTRYPOINT ["/usr/bin/php", "/tmp/run.php"]  

