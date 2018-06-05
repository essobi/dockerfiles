FROM ubuntu:14.04  
MAINTAINER Ian Babrou <ibobrik@gmail.com>  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get --no-install-recommends -y install collectd libpython2.7 python-pip
git-core  
  
RUN pip install envtpl  
ADD collectd.conf.tpl /etc/collectd/collectd.conf.tpl  
  
RUN git clone https://github.com/phobos182/collectd-elasticsearch.git
/usr/share/collectd/plugins/elasticsearch  
  
ADD ./run.sh /run.sh  
CMD /run.sh  

