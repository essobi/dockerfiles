FROM alpine:3.4  
RUN apk --no-cache add ucarp  
  
ENV UCARP_INTERFACE eth0  
ENV UCARP_SOURCEADDRESS 10.10.10.10  
ENV UCARP_VIRTUALADDRESS 10.10.10.20  
ENV UCARP_VIRTUALPREFIX 24  
ENV UCARP_VHID 123  
ENV UCARP_PASS "pass1234"  
ENV UCARP_UPSCRIPT /etc/ucarp/vip-up-default.sh  
ENV UCARP_DOWNSCRIPT /etc/ucarp/vip-down-default.sh  
ENV UCARP_OPTS "--shutdown"  
COPY start.sh /start.sh  
  
CMD [ "./start.sh" ]  

