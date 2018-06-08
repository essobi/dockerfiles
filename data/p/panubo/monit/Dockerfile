FROM alpine:latest  
  
COPY monit /etc/monit  
COPY checks /etc/monit/checks  
COPY entry.sh /  
  
RUN apk add -U monit bash util-linux lvm2 && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /var/lib/monit/events && \  
chmod 700 /etc/monit/monitrc && \  
chmod +x /etc/monit/checks/* && \  
# Cache config  
cp -a /etc/monit/conf.d /etc/monit/conf.d.cache  
  
#VOLUME /etc/monit /var/lib/monit  
EXPOSE 2812  
ENTRYPOINT ["/entry.sh"]  
  
CMD ["monit", "-I", "-c", "/etc/monit/monitrc"]  

