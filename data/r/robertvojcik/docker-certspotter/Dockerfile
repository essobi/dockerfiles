FROM golang:1.10  
RUN go get software.sslmate.com/src/certspotter/cmd/certspotter  
RUN mkdir -p /certspotter/  
  
ADD run.sh /  
  
# Additional package for mailing  
RUN apt-get update  
RUN apt-get install -y mutt  
RUN apt-get clean  
  
WORKDIR /certspotter  
  
CMD ["/run.sh"]  

