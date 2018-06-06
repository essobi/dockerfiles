FROM ubuntu:12.04.5  
  
# define Docker image label information  
LABEL com.ciandt.vendor="CI&T Software SA" \  
com.ciandt.maintainers.1="Ivan Pinatti - @ivan_pinatti" \  
com.ciandt.maintainers.2="Thomas Bryan - @thobryan"  
  
# defines root user, to perform privileged operations  
USER root  
  
# enable apt mirrors (best performance due to use the closest repository)  
RUN readonly APT_SOURCES="/etc/apt/sources.list" \  
&& readonly UBUNTU_RELEASE_NAME="$(cat /etc/lsb-release | grep CODENAME | cut
-d '=' -f2)" \  
&& sed --in-place \  
\--regexp-extended \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\.ubuntu\.com\/mirrors\.txt
"${UBUNTU_RELEASE_NAME}"-security main restricted universe multiverse\n\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\.ubuntu\.com\/mirrors\.txt
"${UBUNTU_RELEASE_NAME}"-backports main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\.ubuntu\.com\/mirrors\.txt
"${UBUNTU_RELEASE_NAME}"-updates main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\.ubuntu\.com\/mirrors\.txt
"${UBUNTU_RELEASE_NAME}" main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/\# Enable Ubuntu mirrors and multiverse\n/" \  
"${APT_SOURCES}"  
  
# upgrade Ubuntu packages, install security updates and required packages  
RUN readonly UBUNTU_PACKAGES=" \  
curl \  
" \  
&& apt-get update \  
&& apt-get upgrade --assume-yes \  
&& apt-get install --no-install-recommends \  
\--assume-yes \  
${UBUNTU_PACKAGES} \  
# remove apt cache in order to improve Docker image size  
&& apt-get clean  
  
## Solr  
# environment variables  
ENV SOLR_VERSION 4.5.1  
ENV SOLR_USER solr  
ENV SOLR_UID 8983  
ENV SOLR_PORT 8983  
ENV DRUPAL_SEARCH_API_SOLR_VERSION 7.x-1.12  
  
# declare required packages  
RUN readonly SOLR_PACKAGES=" \  
openjdk-6-jre-headless \  
tomcat6 \  
" \  
# install packages  
&& apt-get update \  
&& apt-get install \  
\--no-install-recommends \  
\--assume-yes \  
${SOLR_PACKAGES} \  
# remove apt cache in order to improve Docker image size  
&& apt-get clean  
  
# create group  
RUN groupadd \  
\--system \  
\--gid ${SOLR_UID} \  
${SOLR_USER} \  
# create user and add to group  
&& useradd \  
\--system \  
\--uid ${SOLR_UID} \  
\--gid ${SOLR_USER} \  
${SOLR_USER}  
  
# create temp folder  
RUN mkdir /tmp/solr \  
&& cd /tmp/solr \  
# download Solr  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--output solr-${SOLR_VERSION}.tgz \  
https://archive.apache.org/dist/lucene/solr/${SOLR_VERSION}/solr-${SOLR_VERSION}.tgz
\  
# extract Solr  
&& tar \  
\--extract \  
\--gunzip \  
\--file \  
solr-${SOLR_VERSION}.tgz \  
\--directory \  
/opt \  
# link Solr folder  
&& ln \  
\--symbolic \  
\--force \  
/opt/solr-${SOLR_VERSION} \  
/opt/solr \  
# download Drupal search API for Solr  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--output search_api_solr-${DRUPAL_SEARCH_API_SOLR_VERSION}.tar.gz \  
https://ftp.drupal.org/files/projects/search_api_solr-${DRUPAL_SEARCH_API_SOLR_VERSION}.tar.gz
\  
# create folder for Drupal search API  
&& mkdir \  
\--parents \  
/opt/solr/example/solr/collection1/conf \  
# extract Drupal search API for Solr  
&& tar \  
\--extract \  
\--gunzip \  
\--directory \  
/opt/solr/example/solr/collection1/conf \  
\--strip-components 3 \  
\--file \  
search_api_solr-${DRUPAL_SEARCH_API_SOLR_VERSION}.tar.gz \  
search_api_solr/solr-conf/4.x \  
# change permissions  
&& chown \  
\--recursive \  
${SOLR_USER}:${SOLR_USER} \  
/opt/solr-${SOLR_VERSION} \  
&& chown \  
\--recursive \  
${SOLR_USER}:${SOLR_USER} \  
/opt/solr \  
# purge source files  
&& cd / \  
&& rm \  
\--recursive \  
\--force \  
/tmp/solr  
  
## DUMB-init  
# more information at: https://github.com/Yelp/dumb-init  
  
# environment variables  
ENV DUMB_INIT_VERSION 1.2.0  
  
# download  
RUN mkdir \  
\--parents \  
/tmp/dumb-init \  
&& cd /tmp/dumb-init \  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64.deb \  
# install  
&& dpkg \  
\--install \  
dumb-init_${DUMB_INIT_VERSION}_amd64.deb \  
# remove temp folder  
&& cd / \  
&& rm \  
\--force \  
\--recursive \  
/tmp/dumb-init  
  
## Docker specifics  
# expose Solr service port  
EXPOSE ${SOLR_PORT}  
  
# drop back to the regular Solr user - good practice  
USER ${SOLR_USER}  
  
# change workdir to Solr folder  
WORKDIR /opt/solr/example  
  
# docker entrypoint/cmd configuration  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["java","-Xmx256m","-jar","start.jar"]  

