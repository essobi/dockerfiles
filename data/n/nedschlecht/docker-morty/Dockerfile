FROM golang:alpine  
  
RUN apk update && apk add git && rm -rf /var/cache/apk/*  
  
RUN go get github.com/asciimoo/morty  
  
EXPOSE 3000  
COPY run.sh /run.sh  
  
CMD ["/run.sh"]  

