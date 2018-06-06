FROM node:0.12  
COPY . /root/  
RUN cd /root/; npm install --production  
RUN apt-get update -qy  
RUN apt-get install -qy vim nmap iptraf htop  
EXPOSE 3000  
WORKDIR '/root'  
CMD ["./bootstrap.sh"]  

