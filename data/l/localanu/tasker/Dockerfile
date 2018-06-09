FROM golang:1.8-jessie  
MAINTAINER Mochammad Nur Afandi (localanu@gmail.com)  
  
RUN apt update && apt install -y sqlite3  
  
WORKDIR /go/src/app  
COPY . .  
RUN go-wrapper download  
RUN go-wrapper install  
RUN sqlite3 tasks.db < schema.sql  
  
CMD ["go-wrapper", "run"]  

