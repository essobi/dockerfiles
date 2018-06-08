FROM debian:jessie  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends snmp
wget ca-certificates && \  
rm -rf /var/lib/apt/lists/* && \  
echo 'hosts: files dns' >> /etc/nsswitch.conf  
  
ENV TELEGRAF_VERSION 1.4.0-nfsclient  
  
RUN set -ex && \  
wget -q
https://dl.skinfra.cloud/monitoring/telegraf/telegraf-${TELEGRAF_VERSION}-static_linux_amd64
&& \  
mv telegraf-${TELEGRAF_VERSION}-static_linux_amd64 /usr/bin/telegraf && \  
chmod +x /usr/bin/telegraf && \  
mkdir -p /etc/telegraf && \  
/usr/bin/telegraf config > /etc/telegraf/telegraf.conf  
  
EXPOSE 8125/udp 8092/udp 8094  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["telegraf"]  

