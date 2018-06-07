FROM phusion/passenger-full  
  
ADD bootstrap.sh /tmp/  
ADD config.js /tmp/  
ADD default /tmp/  
ADD kiwiirc.run /tmp/  
RUN chmod +x /tmp/bootstrap.sh ; /tmp/bootstrap.sh;  
  
EXPOSE 7778 7777 80 443  
  
#ENTRYPOINT ["./kiwi", "-f", "start"]  
#CMD ["-c", "config.js"]  
CMD ["/sbin/my_init"]  

