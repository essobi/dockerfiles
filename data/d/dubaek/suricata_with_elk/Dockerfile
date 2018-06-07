FROM dubaek/ubuntu  
MAINTAINER doun baek <dubaek@gmail.com>  
  
RUN apt-get -qqy install libpcre3 \  
libpcre3-dbg libpcre3-dev \  
build-essential autoconf automake libtool \  
libpcap-dev libnet1-dev \  
libyaml-0-2 libyaml-dev zlib1g zlib1g-dev \  
libcap-ng-dev libcap-ng0 \  
make libmagic-dev libjansson-dev libjansson4 \  
pkg-config  
  
# install suricata  
# following url : https://hackertarget.com/install-suricata-ubuntu-5-minutes/  
RUN wget http://www.openinfosecfoundation.org/download/suricata-2.0.11.tar.gz  
RUN tar xvzf suricata-2.0.11.tar.gz  
  
WORKDIR suricata-2.0.11  
RUN ./configure && make && make install-full && ldconfig  
RUN mkdir /etc/suricata  
RUN mkdir /var/log/suricata  
RUN pwd  
RUN cp classification.config /etc/suricata  
RUN cp reference.config /etc/suricata  
RUN cp suricata.yaml /etc/suricata  
  
RUN wget http://rules.emergingthreats.net/open/suricata/emerging.rules.tar.gz  
RUN tar zxvf emerging.rules.tar.gz  
RUN cp -r rules /etc/suricata/  
  
# install elk  
#
https://gist.githubusercontent.com/thisismitch/8b15ac909aed214ad04a/raw/fc5025c3fc499ad8262aff34ba7fde8c87ead7c0/kibana-4.x-init  
WORKDIR /  
RUN apt-get -qqy install nginx openjdk-7-jdk openjdk-7-jre-headless  
RUN wget
https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.1.1/elasticsearch-2.1.1.deb  
RUN wget
https://download.elastic.co/logstash/logstash/packages/debian/logstash_2.1.1-1_all.deb  
RUN wget
https://download.elastic.co/kibana/kibana/kibana-4.3.1-linux-x64.tar.gz  
  
RUN dpkg -i elasticsearch-2.1.1.deb  
RUN dpkg -i logstash_2.1.1-1_all.deb  
RUN tar -xzvf kibana-4.3.1-linux-x64.tar.gz  
  
ADD logstash.conf /etc/logstash/conf.d/logstash.conf  
  
# run services  
ADD start.sh /tmp/start.sh  
CMD /tmp/start.sh  
  
EXPOSE 80  

