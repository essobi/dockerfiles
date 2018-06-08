FROM ubuntu:12.04  
MAINTAINER Eunchong Yu <kroisse@smartstudy.co.kr>  
  
ADD RPM-GPG-KEY-td-agent /tmp/RPM-GPG-KEY-td-agent  
RUN apt-key add /tmp/RPM-GPG-KEY-td-agent && rm /tmp/RPM-GPG-KEY-td-agent  
RUN echo "deb http://packages.treasure-data.com/precise/ precise contrib" >
/etc/apt/sources.list.d/treasure-data.list && \  
apt-get update && \  
apt-get install -y --force-yes libssl0.9.8 td-agent && \  
apt-get clean  
ENV GEM_HOME /usr/lib/fluent/ruby/lib/ruby/gems/1.9.1/  
ENV GEM_PATH /usr/lib/fluent/ruby/lib/ruby/gems/1.9.1/  
ENV PATH /usr/lib/fluent/ruby/bin:$PATH  
RUN fluentd --setup=/etc/fluent && \  
mkdir -p /var/log/fluent  
  
EXPOSE 24224  
CMD ["fluentd", "--conf=/etc/fluent/fluent.conf"]  

