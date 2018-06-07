FROM phusion/baseimage:0.9.17  
MAINTAINER Damien Garros <dgarros@gmail.com>  
  
RUN apt-get -y update && \  
apt-get -y upgrade  
  
# dependencies  
RUN apt-get -y --force-yes install \  
git adduser libfontconfig wget ruby ruby-dev make curl \  
build-essential tcpdump  
  
########################  
### Install Fluentd ###  
########################  
  
RUN gem install fluentd statsd-ruby rake bundler --no-ri --no-rdoc && \  
gem install dogstatsd-ruby  
  
RUN mkdir /etc/fluent && \  
mkdir /etc/fluent/plugin  
  
ADD fluentd/fluent.conf /fluent/fluent.conf  
RUN fluentd --setup ./fluent  
  
## Install plugin  
ADD fluentd/out_statsd.rb /etc/fluent/plugin/out_statsd.rb  
  
RUN git clone https://github.com/JNPRAutomate/fluent-plugin-juniper-
telemetry.git && \  
cd fluent-plugin-juniper-telemetry && \  
rake install  
  
ADD fluentd/fluentd.launcher.sh /etc/service/fluentd/run  
RUN chmod +x /etc/service/fluentd/run  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV HOME /root  
RUN chmod -R 777 /var/log/  
  
## Fluentd  
EXPOSE 51020  
  
CMD ["/sbin/my_init"]  

