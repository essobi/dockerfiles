FROM golang:latest  
RUN mkdir /app  
ADD . /app/  
WORKDIR /app  
RUN go build -o delay-server .  
EXPOSE 8080  
CMD ["/app/delay-server"]

