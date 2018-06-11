FROM alpine:3.4  
RUN apk --no-cache add dnsmasq rsyslog  
EXPOSE 53 53/udp  
COPY ./run.sh /bin/run.sh  
RUN chmod a+x /bin/run.sh  
ENTRYPOINT ["ash", "/bin/run.sh"]  

