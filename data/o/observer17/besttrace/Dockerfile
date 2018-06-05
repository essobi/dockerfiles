FROM debian  
RUN apt update && apt install wget -y  
COPY ./besttrace /usr/bin/besttrace  
RUN chmod +x /usr/bin/besttrace  
ENTRYPOINT ["/usr/bin/besttrace"]  

