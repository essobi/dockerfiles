FROM openjdk:8-jre-alpine  
MAINTAINER Claudio Ramirez <pub.claudio@gmail.com>  
  
### Environment ###  
#ENV app=idp \  
ENV \  
version=3.3.2 \  
idp_sha256="ed9fbefd273199d2841d4045b2661671c53825ed3c7d52d38bfe516b39d5fc64"
\  
idp_baseurl="https://shibboleth.net/downloads/identity-provider" \  
PATH=/opt/idp/bin:$PATH  
  
### Run ###  
RUN \  
set -xv; \  
export IDP_URL="${idp_baseurl}/${version}/shibboleth-identity-
provider-${version}.tar.gz"; \  
apk add --no-cache bash curl && \  
# Download IDP  
curl -s -L $IDP_URL -o idp.tar.gz && sha256sum idp.tar.gz && \  
echo "${idp_sha256} idp.tar.gz" | sha256sum -c - && \  
mkdir /opt && tar xzf idp.tar.gz -C /opt && mv /opt/shib* /opt/idp &&\  
# Cleanup  
cd /opt/idp && rm -rf `ls -1 |grep -v ^'bin\|webapp'` && \  
cd /opt/idp/bin && rm -rf `ls -1 |grep -v ^'seckeygen.sh\|runclass.sh'` && \  
cd /opt/idp/webapp && rm -rf `ls -1 |grep -v ^'WEB-INF'` && \  
cd /opt/idp/webapp/WEB-INF && rm -rf `ls -1 |grep -v ^'lib'` && \  
cd /opt/idp/webapp/WEB-INF/lib && rm -rf `ls -1 | \  
grep -v ^'idp-core\|java-support\|jcommander\|logback-classic\|logback-
core\|slf4j-api'` && \  
rm -f /opt/idp.tar.gz && apk del curl  
  
### Working directory ###  
WORKDIR /mnt  

