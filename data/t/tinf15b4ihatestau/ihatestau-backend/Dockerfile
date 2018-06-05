FROM debian:stretch  
  
ADD . /ihatestau-source  
  
RUN /ihatestau-source/docker-supp/setup-script.sh  
  
USER ihatestau  
  
EXPOSE 8080  
WORKDIR /tmp  
  
CMD ["supervisord", "-c", "/home/ihatestau/supervisor.conf"]  
  

