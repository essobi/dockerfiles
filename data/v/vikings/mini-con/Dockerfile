FROM golang:1.8  
  
RUN apt-get update && \  
apt-get install -y expect && \  
go get -u github.com/golang/dep/... && \  
wget -O /Mini_con "https://www.dropbox.com/s/g1iruzvhbgyhoge/Mini-con?dl=0" &&
\  
chmod 755 /Mini_con  
  
EXPOSE 80  
  
CMD ["/Mini_con"]  
  

