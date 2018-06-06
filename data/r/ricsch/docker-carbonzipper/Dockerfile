FROM ubuntu:14.10  
ENV CARBONZIPPER_PORT 8085  
ADD carbonzipper /bin/carbonzipper  
ADD start.sh /bin/start.sh  
ADD zipper.json /zipper.json  
  
ENTRYPOINT /bin/start.sh  

