FROM alpine:3.7  
RUN apk add --update umurmur && rm -rf /var/cache/apk/*  
  
COPY conf/umurmur.conf /etc/umurmur/umurmur.conf  
COPY conf/channels.conf /etc/umurmur/channels.conf  
  
COPY setup.sh /  
RUN chmod +x /setup.sh  
  
EXPOSE 64738  
EXPOSE 64738/udp  
  
CMD /setup.sh && umurmurd -d -c /etc/umurmur/umurmur.conf  

