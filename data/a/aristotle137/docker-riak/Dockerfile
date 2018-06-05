FROM ubuntu:14.04  
MAINTAINER Marius Cobzarenco <marius@reinfer.io>  
  
# Environmental variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV RIAK_VERSION 2.1.1-1  
# Install dependencies for Riak and Erlang  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update -qq && apt-get install -y software-properties-common && \  
apt-add-repository ppa:webupd8team/java -y && apt-get update -qq && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java7-installer build-essential autoconf
libncurses5-dev openssl libssl-dev fop xsltproc unixodbc-dev curl  
  
RUN mkdir /src  
WORKDIR /src  
  
#Install Erlang  
RUN wget
http://s3.amazonaws.com/downloads.basho.com/erlang/otp_src_R16B02-basho8.tar.gz
&& \  
tar zxvf otp_src_R16B02-basho8.tar.gz && \  
cd OTP_R16B02_basho8 && \  
./otp_build autoconf && \  
./configure && make && make install  
  
# Install Riak  
RUN curl --silent
https://packagecloud.io/install/repositories/basho/riak/script.deb.sh | bash  
RUN apt-get update -qq && apt-get install -y riak=${RIAK_VERSION}  
  
ADD etc/riak.conf /etc/riak/riak.conf  
ADD etc/advanced.config /etc/riak/advanced.config  
  
# Add and compile beams  
RUN mkdir -p /opt/riak/beams  
ADD ./beams /opt/riak/beams  
WORKDIR /opt/riak/beams  
RUN erlc *.erl  
  
# Add Solr schemas  
RUN mkdir -p /opt/riak/schemas  
ADD ./schemas /opt/riak/schemas  
  
# Create schemas, indexes and bucket types  
ADD ./set_nodename.sh /opt/riak/set_nodename.sh  
ADD ./create_bucket_types.sh /opt/riak/create_bucket_types.sh  
WORKDIR /opt/riak  
  
RUN riak start && ./create_bucket_types.sh && riak stop  
  
RUN apt-get update -qq && apt-get -y build-dep pam  
RUN export CONFIGURE_OPTS=--disable-audit && cd /root && apt-get -b source pam
&& dpkg -i libpam-doc*.deb libpam-modules*.deb libpam-runtime*.deb
libpam0g*.deb  
  
VOLUME ["/var/lib/riak"]  
EXPOSE 8069 8087 8098  
CMD ulimit -n 65536 && \  
riak start && \  
tail -f /var/log/riak/console.log  

