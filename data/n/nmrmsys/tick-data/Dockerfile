# nmrmsys/tick-data - TICK Stack pre-configured Data Volume Container  
FROM alpine  
MAINTAINER nmrmsys@gmail.com  
  
RUN mkdir -p /root/tick-conf  
ADD tick-conf /root/tick-conf/  
  
ADD cmd.sh /root/cmd.sh  
CMD /root/cmd.sh  

