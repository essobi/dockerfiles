FROM gregory90/golang:1.4  
  
RUN go get -u github.com/mattes/migrate  
RUN apt-get update && apt-get install -y mysql-client  
  
ENTRYPOINT ["migrate"]  

