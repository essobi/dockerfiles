FROM rimmon1971/base-alpine:3.7-20180228  
LABEL product="haproxy-1.7.9-r1"  
  
EXPOSE 80  
RUN apk --no-cache add haproxy  
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]  

