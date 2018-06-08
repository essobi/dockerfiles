FROM ubuntu:14.04  
MAINTAINER Takayuki Shimizukawa shimizukawa@gmail.com  
  
# install curl and fluentd deps  
RUN apt-get update \  
&& apt-get install -y curl libcurl4-openssl-dev ruby ruby-dev make \  
&& apt-get clean  
  
# install fluentd with plugins  
RUN gem install fluentd --no-ri --no-rdoc \  
&& fluent-gem install fluent-plugin-elasticsearch \  
fluent-plugin-record-modifier fluent-plugin-exclude-filter  
  
RUN mkdir -p /var/log/fluentd && mkdir -p /etc/fluentd  
  
# add conf  
ADD ./bin /app/bin  
ADD ./config /app/config  
  
WORKDIR /app  
  
ENV ES_HOST localhost  
ENV ES_PORT 9200  
  
CMD [ "/bin/bash", "/app/bin/start" ]  
  

