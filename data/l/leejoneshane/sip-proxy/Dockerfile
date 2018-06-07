FROM debian  
MAINTAINER leejoneshane@gmail.com  
  
RUN apt-get update \  
&& apt-get -y install gawk curl vim build-essential \  
&& apt-get clean all \  
&& cd /root \  
&& curl http://www.antisip.com/download/exosip2/libosip2-5.0.0.tar.gz -o
libosip2.tar.gz \  
&& tar -xzf libosip2.tar.gz \  
&& rm -rf libosip2.tar.gz \  
&& cd libosip2-5.0.0 \  
&& ./configure \  
&& make \  
&& make install  
  
ADD siproxd-0.8.2.tar.gz /root  
RUN cd /root/siproxd-0.8.2 \  
&& ./configure \  
&& make \  
&& make install  
  
ADD siproxd.conf /etc  
ADD run-siproxd.sh /usr/sbin  
RUN chmod +x /usr/sbin/run-siproxd.sh \  
&& mkdir /var/lib/siproxd \  
&& touch /var/lib/siproxd/siproxd_registrations  
EXPOSE 5060/udp 7070-7089/udp  
CMD ["run-siproxd.sh"]  

