FROM debian:jessie  
  
WORKDIR /  
COPY cmd.sh cmd.sh  
RUN chmod a+x cmd.sh  
  
WORKDIR /secret  
CMD /cmd.sh && tail -f /dev/null  

