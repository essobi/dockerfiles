FROM debian:jessie  
  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
RUN apt-get update \  
&& apt-get install -y teeworlds-server \  
&& apt-get clean all  
  
COPY teeworlds_basket_srv /usr/games/teeworlds-server  
RUN chmod +x /usr/games/teeworlds-server  
  
COPY ctf.cfg /ctf.cfg  
  
EXPOSE 8303/udp  
CMD ["/run.sh"]  

