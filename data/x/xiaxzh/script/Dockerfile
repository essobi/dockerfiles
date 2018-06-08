# Build on golang:1.9  
FROM golang:1.9  
# Create a diretory to save our files  
RUN mkdir -p /go/src/service-end  
WORKDIR /go/src/service-end  
  
# Copy source code  
COPY . /go/src/service-end  
  
RUN go-wrapper download && go-wrapper install  
  
# Setting ENV Value  
ENV PORT 8080  
# Expose 8080 port to communicate with host  
# Containner Begin  
CMD ["go-wrapper", "run"]

