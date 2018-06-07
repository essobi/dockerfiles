FROM telegraf  
  
RUN apt-get update && \  
apt-get -y install ipmitool  
  
EXPOSE 8125/udp 8092/udp 8094  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["telegraf"]  
  

