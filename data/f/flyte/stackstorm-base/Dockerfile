FROM ubuntu:xenial  
  
ARG ST2_VERSION=2.1.1-1  
ARG ST2_REPO=stable  
ARG
ST2_PACKAGE=https://packagecloud.io/StackStorm/${ST2_REPO}/packages/ubuntu/xenial/st2_${ST2_VERSION}_amd64.deb/download  
  
LABEL com.stackstorm.version="${ST2_VERSION}"  
  
RUN apt-get -y update && apt-get -y install adduser procps python2.7 libffi6
libyaml-0-2 git libpcre3 libpython2.7 libxml2 python-dev libssl-dev libffi-dev
sudo build-essential  
  
ADD ${ST2_PACKAGE} /tmp/st2_${ST2_VERSION}_amd64.deb  
RUN dpkg -i /tmp/st2_${ST2_VERSION}_amd64.deb && rm -r
/tmp/st2_${ST2_VERSION}_amd64.deb && apt-get clean  
  
ADD ./st2.conf.template /st2.conf.template  
RUN md5sum /etc/st2/st2.conf > /st2.conf.orig.md5  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
VOLUME [ "/etc/st2", "/opt/stackstorm/packs" ]  
ENTRYPOINT [ "/entrypoint.sh" ]  

