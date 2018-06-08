FROM golang:onbuild  
  
RUN apt-get update && \  
apt-get install -y openssh-client && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 22  
  
ENTRYPOINT ["passage"]  

