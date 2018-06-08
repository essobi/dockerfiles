FROM debian  
MAINTAINER danielguerra, https://github.com/danielguerra/packetbroker  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get -yq update \  
&& apt-get -yq upgrade \  
&& apt-get install -yq libnet-pcap-perl wget make gcc libmath-int64-perl
supervisor xinetd \  
&& cd /tmp \  
&& wget http://search.cpan.org/CPAN/authors/id/M/MA/MARKELLIS/Net-AMQP-
RabbitMQ-2.200000.tar.gz \  
&& tar xvfz Net-AMQP-RabbitMQ-2.200000.tar.gz \  
&& cd /tmp/Net-AMQP-RabbitMQ-2.200000 \  
&& perl Makefile.PL \  
&& make \  
&& make install \  
&& apt-get remove -y make gcc \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN echo "packetbroker 1969/tcp # pcap amqp feed" >> /etc/services  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD packetbroker /etc/xinetd.d/packetbroker  
ADD initamqp /bin/initamqp  
ADD pcap2amqp /bin/pcap2amqp  
ADD broker /bin/broker  
ADD amqp2pcap /bin/amqp2pcap  
ADD consumer /bin/consumer  
EXPOSE 1969  
CMD ["/bin/bash"]  

