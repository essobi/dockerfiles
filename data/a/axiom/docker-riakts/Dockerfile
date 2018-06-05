FROM phusion/baseimage:0.9.22  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
ENV KILL_PROCESS_TIMEOUT 60  
ENV KILL_ALL_PROCESS_TIMEOUT 60  
MAINTAINER Kyle Wilcox <kyle@axiomdatascience.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
# Setup Riak  
ENV RIAK_VERSION 1.5.2  
ENV OS_FAMILY ubuntu  
ENV OS_VERSION 14.04  
ENV OS_FLAVOR xenial  
ENV RIAK_HOME /usr/lib/riak  
ENV RIAK_DATA /var/lib/riak  
ENV RIAK_LOGS /var/log/riak  
ENV RIAK_SCHEMAS /etc/riak/schemas  
ENV RIAK_CONFIG /etc/riak/riak.conf  
ENV RIAK_USER_CONFIG /etc/riak/user.conf  
ENV RIAK_KEY https://packagecloud.io/basho/riak-ts/gpgkey  
  
RUN curl -L "${RIAK_KEY}" | apt-key add - && \  
echo "deb https://packagecloud.io/basho/riak-ts/${OS_FAMILY}/ ${OS_FLAVOR}
main" | tee /etc/apt/sources.list.d/basho_riak-ts.list && \  
echo "deb-src https://packagecloud.io/basho/riak-ts/${OS_FAMILY}/ ${OS_FLAVOR}
main" | tee -a /etc/apt/sources.list.d/basho_riak-ts.list && \  
apt-get update && \  
apt-get install -y \  
apt-transport-https \  
binutils \  
build-essential \  
bzip2 \  
ca-certificates \  
curl \  
debian-archive-keyring \  
riak-ts=${RIAK_VERSION}-1 \  
&& \  
mkdir -p ${RIAK_SCHEMAS} && \  
mkdir -p ${RIAK_LOGS} && \  
rm -rf /etc/service/cron && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PATH $RIAK_HOME/bin:$PATH  
  
VOLUME [ "${RIAK_DATA}", "${RIAK_LOGS}", "${RIAK_SCHEMAS}" ]  
  
EXPOSE 8087  
EXPOSE 8098  
WORKDIR ${RIAK_DATA}  
  
COPY init/* /etc/my_init.d/  
COPY riakts.sh /etc/service/riak/run  

