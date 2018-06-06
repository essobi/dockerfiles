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
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}"-security main restricted universe multiverse\n\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}"-backports main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}"-updates main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}" main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/\\# Enable Ubuntu mirrors and multiverse\n/" \  
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
  
## Memcached  
# environment variables  
ENV MEMCACHED_VERSION 1.4.13  
# declare required packages  
RUN readonly MEMCACHED_PACKAGES=" \  
memcached=${MEMCACHED_VERSION}-* \  
" \  
# install packages  
&& apt-get install \  
\--no-install-recommends \  
\--assume-yes \  
${MEMCACHED_PACKAGES} \  
# remove apt cache in order to improve Docker image size  
&& apt-get clean  
  
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
# expose Memcached service port  
EXPOSE 11211  
# drop back to the regular Memcached user - good practice  
USER memcache  
  
# change workdir  
WORKDIR /  
  
# docker entrypoint/cmd configuration  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["memcached"]  

