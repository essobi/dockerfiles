FROM yobasystems/alpine:i386  
  
ENV ARCH=x86  
  
RUN apk --update add perl-dev python3-dev wget alpine-sdk linux-headers
rsyslog rrdtool rrdtool-dev rrdtool-utils  
  
# Get and untar sources files  
RUN wget https://collectd.org/files/collectd-5.7.2.tar.bz2  
RUN tar jxvf collectd-5.7.2.tar.bz2 && rm collectd-5.7.2.tar.bz2  
  
# Compile and purge source files  
RUN cd collectd-5.7.2 && ./configure --with-rrdtool && make all install  
RUN cd .. && rm -rf collectd-5.7.2  
  
# Optionnal post installation tasks  
RUN ln -s /opt/collectd/sbin/collectd /usr/sbin/collectd  
RUN ln -s /opt/collectd/sbin/collectdmon /usr/sbin/collectdmon  
  
RUN rm -rf /var/cache/apk/*  
RUN apk del linux-headers perl-dev python3-dev alpine-sdk  
  
ADD ./etc/collectd /etc/collectd  
ADD ./entrypoint.sh /entrypoint.sh  
  
VOLUME /etc/collectd  
  
ENTRYPOINT ["/entrypoint.sh"]  

