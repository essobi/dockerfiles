FROM ubuntu:14.04  
MAINTAINER Analyser <analyser@gmail.com>  
LABEL Description="Fluentd Docker Image" Vendor="Analyser" Version="1.0.1"  
  
RUN apt-get update -y && \  
apt-get install -y \  
autoconf \  
bison \  
build-essential \  
curl \  
git \  
libffi-dev \  
libgdbm3 \  
libgdbm-dev \  
libncurses5-dev \  
libreadline6-dev \  
libssl-dev \  
libyaml-dev \  
zlib1g-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# for log storage (maybe shared with host)  
RUN mkdir -p /fluentd/log  
# configuration/plugins path (default: copied from .)  
RUN mkdir -p /fluentd/etc  
RUN mkdir -p /fluentd/plugins  
  
RUN mkdir -p /opt/ruby  
WORKDIR /tmp  
  
RUN git clone https://github.com/tagomoris/xbuild.git /tmp/.xbuild  
RUN /tmp/.xbuild/ruby-install 2.2.2 /opt/ruby  
RUN rm -fr /tmp/.xbuild  
  
ENV PATH /opt/ruby/bin:$PATH  
RUN gem install fluentd -v 0.12.16 --no-rdoc --no-ri  
  
RUN gem install fluent-plugin-elasticsearch --no-rdoc --no-ri  
RUN gem install fluent-plugin-record-reformer --no-rdoc --no-ri  
  
COPY fluent.conf /fluentd/etc/  
ONBUILD COPY fluent.conf /fluentd/etc/  
ONBUILD COPY plugins/ /fluentd/plugins/  
  
WORKDIR /opt  
  
ENV FLUENTD_OPT=""  
ENV FLUENTD_CONF="fluent.conf"  
EXPOSE 24224  
### docker run -p 24224 -v `pwd`/log: -v `pwd`/log:/home/ubuntu/log
fluent/fluentd:latest  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT  

