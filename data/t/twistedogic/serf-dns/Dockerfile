FROM google/debian:wheezy  
MAINTAINER Jordan Li  
  
ENV SERF_HOME /root/serf  
RUN mkdir $SERF_HOME && mkdir $SERF_HOME/bin && mkdir $SERF_HOME/etc  
  
RUN apt-get update -y && apt-get install -y wget unzip curl dnsmasq  
RUN echo "user=root" > /etc/dnsmasq.conf  
RUN echo "addn-hosts=/etc/althosts" >> /etc/dnsmasq.conf  
RUN echo "listen-address=0.0.0.0" >> /etc/dnsmasq.conf  
RUN echo "resolv-file=/etc/resolv.dnsmasq.conf" >> /etc/dnsmasq.conf  
RUN echo "bind-interfaces" >> /etc/dnsmasq.conf  
RUN echo "expand-hosts" >> /etc/dnsmasq.conf  
RUN echo "port=53" >> /etc/dnsmasq.conf  
RUN echo "log-queries" >> /etc/dnsmasq.conf  
RUN echo "resolv-file=/etc/resolv.dnsmasq.conf" >> /etc/dnsmasq.conf  
RUN echo "conf-dir=/etc/dnsmasq.d" >> /etc/dnsmasq.conf  
  
RUN echo "nameserver 8.8.8.8" > /etc/resolv.dnsmasq.conf  
  
RUN wget https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip -P /tmp  
RUN unzip /tmp/0.6.4_linux_amd64.zip -d $SERF_HOME/bin && rm -f
/tmp/0.6.4_linux_amd64.zip  
  
COPY serf_init.sh $SERF_HOME/bin/serf_init.sh  
COPY dnsmasq.json $SERF_HOME/etc/dnsmasq.json  
COPY dnsmasq.sh $SERF_HOME/bin/dnsmasq.sh  
RUN chmod +x $SERF_HOME/bin/*  
  
EXPOSE 53 7946  
CMD /root/serf/bin/serf_init.sh  
  

