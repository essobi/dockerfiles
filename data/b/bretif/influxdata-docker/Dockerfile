FROM alpine:3.5  
ENV TELEGRAF_VERSION 1.2.1-sdk.1  
RUN apk add --no-cache ca-certificates && \  
update-ca-certificates  
  
RUN apk add --no-cache --virtual .build-deps wget gnupg tar && \  
wget -q
http://dl.skinfra.cloud/monitoring/telegraf/telegraf-${TELEGRAF_VERSION}-static_linux_amd64
&& \  
mv telegraf-${TELEGRAF_VERSION}-static_linux_amd64 telegraf && \  
chmod +x telegraf && \  
mkdir -p /etc/telegraf && \  
cp -a telegraf /usr/bin/ && \  
/usr/bin/telegraf config > /etc/telegraf/telegraf.conf && \  
apk del .build-deps  
  
EXPOSE 8125/udp 8092/udp 8094  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["telegraf"]  

