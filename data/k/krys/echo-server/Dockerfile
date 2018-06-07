FROM golang:1.7-alpine  
  
RUN mkdir -p /opt/echo-server  
COPY main.go /opt/echo-server/  
RUN cd /opt/echo-server && go build  
  
EXPOSE 8800  
ENTRYPOINT ["/opt/echo-server/echo-server"]  

