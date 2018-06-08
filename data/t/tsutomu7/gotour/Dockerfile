FROM alpine  
  
ENV GOPATH=/root/go  
RUN apk add --update go git && \  
mkdir /root/go && \  
go get golang.org/x/tour/gotour && \  
apk del git && \  
rm /var/cache/apk/*  
EXPOSE 8080  
CMD ["/root/go/bin/gotour", "-http", "0.0.0.0:8080"]  

