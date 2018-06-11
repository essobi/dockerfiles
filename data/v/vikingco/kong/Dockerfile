###########################################################  
# Kong (master rev.) (http://getkong.org)  
###########################################################  
FROM debian:jessie  
MAINTAINER Dirk Moors  
  
ENV KONG_GIT_URL https://github.com/Mashape/kong.git  
ENV KONG_GIT_BRANCH master  
  
ENV KONG_BASE_PKG_VERSION 0.5.2  
ENV KONG_BASE_PKG
https://github.com/Mashape/kong/releases/download/${KONG_BASE_PKG_VERSION}/kong-${KONG_BASE_PKG_VERSION}.jessie_all.deb  
  
ENV DEPENDENCYDIR /tmp/deps  
ENV CONFIGURATIONDIR /tmp/conf  
  
# Add dependencies  
ADD deps ${DEPENDENCYDIR}  
  
# Install Kong  
RUN set -x \  
&& buildDeps=`cat ${DEPENDENCYDIR}/builddeps.txt` \  
&& deps=`cat ${DEPENDENCYDIR}/deps.txt` \  
&& apt-get update \  
&& apt-get install -y ${buildDeps} ${deps} --no-install-recommends \  
&& wget ${KONG_BASE_PKG} \  
&& dpkg -i kong-${KONG_BASE_PKG_VERSION}.*.deb \  
&& rm -rf /etc/kong/ \  
&& rm -rf kong-${KONG_BASE_PKG_VERSION}.*.deb \  
&& git clone ${KONG_GIT_URL} --branch ${KONG_GIT_BRANCH} --single-branch
--depth=1 \  
&& cd kong/ \  
&& make install \  
&& apt-get purge -y --auto-remove ${buildDeps}  
  
# Add config files  
ADD conf ${CONFIGURATIONDIR}  
  
# Make kong config dir  
RUN mkdir -p /etc/kong/  
  
# Link KONG settings  
RUN cd /etc/kong/ \  
&& rm -rf kong.yml \  
&& ln -s ${CONFIGURATIONDIR}/kong.yml  
  
# expose ports  
EXPOSE 8000 8443 8001 8053  
  
# expose run command  
CMD echo "Waiting for cassandra..." \  
&& while ! nc -z cassandra 9042; do sleep 0.1; done \  
&& echo "Cassandra is ready! Launching Kong..." \  
&& kong start \  
&& tail -f /usr/local/kong/logs/error.log  

