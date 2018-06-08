# Pull base image.  
FROM golang:latest  
  
# # Copy a configuration file from the current directory  
RUN mkdir /app  
RUN mkdir /app/db  
ADD . /app/  
WORKDIR /app  
  
# Get Module  
RUN go get github.com/asaskevich/govalidator  
RUN go get github.com/gorilla/handlers  
RUN go get github.com/gorilla/mux  
RUN go get github.com/mattn/go-sqlite3  
  
# Build Go Project  
RUN go build -o main .  
  
# Define default command.  
CMD ["/app/main"]  
  
# Expose ports.  
EXPOSE 1337

