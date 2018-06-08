FROM buildpack-deps:trusty-curl  
  
COPY telegraf_amd64.deb /telegraf_amd64.deb  
  
RUN cd / && dpkg -i telegraf_amd64.deb && \  
rm -f telegraf_amd64.deb*  
  
EXPOSE 8125/udp 8092/udp 8094  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["telegraf"]  

