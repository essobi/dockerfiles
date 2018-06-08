FROM piratenbpt/base  
RUN apt-get install -y bind9  
ADD startup.sh /startup.sh  
EXPOSE 53 53/udp  
ENV FORWARDERS 8.8.8.8 8.8.4.4  
CMD /startup.sh  

