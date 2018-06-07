FROM alpine:3.3  
RUN apk --update add dropbear rsync  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-
init_1.0.1_amd64 /dumb-init  
RUN chmod +x /dumb-init  
ENTRYPOINT ["/dumb-init"]  
  
RUN mkdir /etc/dropbear  
CMD ["dropbear", "-R", "-F", "-E", "-m", "-s"]  

