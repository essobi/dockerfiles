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
  
# Installs OpenJDK-7  
RUN apk --no-cache add openjdk7-jre  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk  
  
# Downloads and installs EviCheck  
ENV EVICHECKPATH /opt/EviCheck  
ENV EVICHECK_URL
http://groups.inf.ed.ac.uk/security/appguarden/tools/EviCheck/EviCheck.tar.gz  
ENV PATH ${EVICHECKPATH}:$PATH  
  
RUN mkdir -p ${EVICHECKPATH} \  
&& curl ${EVICHECK_URL} \--output ${EVICHECKPATH}/evicheck-src.tar.gz \  
&& cd ${EVICHECKPATH} \  
&& tar --strip-components=1 -xvzf evicheck-src.tar.gz \  
&& rm evicheck-src.tar.gz  
  
# Downloads Androguard and required software  
ENV ANDROGUARDPATH ${EVICHECKPATH}/androguard  
ENV PATH ${ANDROGUARDPATH}:$PATH  
  
RUN apk --no-cache add --virtual .compile-dependencies \  
alpine-sdk \  
g++ \  
patch \  
&& apk --no-cache add \  
libxml2 \  
libxml2-dev \  
libxslt \  
libxslt-dev \  
musl-dev \  
py-asn1 \  
py-cryptography \  
py2-pip \  
python \  
python2-dev \  
&& pip install --upgrade pip \  
&& pip install setuptools requests yara future \  
&& pip install git+git://github.com/dweinstein/pyfuzzy@master \  
&& mkdir -p ${ANDROGUARDPATH} \  
&& git clone -b 'v2.0' \--single-branch
https://github.com/androguard/androguard.git ${ANDROGUARDPATH} \  
&& cd ${ANDROGUARDPATH} \  
&& pip install .  
  
# Downloads sat4j and required software  
ENV SAT4J_PATH ${EVICHECKPATH}/solver  
ENV SAT4J_PB_FILENAME sat4j-pb-v20130525.zip  
ENV SAT4J_PB_URL http://download.forge.ow2.org/sat4j/${SAT4J_PB_FILENAME}  
ENV PATH ${SAT4J_PATH}:$PATH  
  
RUN wget ${SAT4J_PB_URL} -O ${SAT4J_PATH}/${SAT4J_PB_FILENAME} \  
&& cd ${SAT4J_PATH} \  
&& unzip ${SAT4J_PB_FILENAME} \  
&& rm ${SAT4J_PB_FILENAME}  
  
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

