FROM alpine  
  
WORKDIR /root  
RUN apk --no-cache add dnsmasq git \  
&& git clone https://git.coding.net/scaffrey/hosts.git  
RUN echo "1 1 * * * cd /root/hosts;git pull >>/root/log"\  
>> /etc/crontabs/root \  
# && echo "addn-hosts=/root/hosts/hosts" >> /etc/dnsmasq.conf \  
&& echo "user=root" >> /etc/dnsmasq.conf \  
&& echo "hostsdir=/root/hosts/hosts-files/" >> /etc/dnsmasq.conf \  
# && echo "port=53" >> /etc/dnsmasq.conf \  
# && echo "no-resolv" >> /etc/dnsmasq.conf \  
&& echo "no-hosts" >> /etc/dnsmasq.conf \  
&& echo "resolv-file=/root/resolv.conf" >> /etc/dnsmasq.conf \  
&& echo "addn-hosts=/root/myhosts" >> /etc/dnsmasq.conf \  
&& echo "nameserver 223.5.5.5">/root/resolv.conf \  
&& echo "nameserver 223.5.5.5">/etc/resolv.conf \  
&& echo "nameserver 114.114.114.114">>/root/resolv.conf \  
&& echo "nameserver 180.76.76.76">>/root/resolv.conf  
EXPOSE 53/udp 53/tcp  
VOLUME /root/myhosts  
USER root  
#CMD crond;dnsmasq -k -q --log-facility=-  
CMD crond;dnsmasq -k --log-facility=-  

