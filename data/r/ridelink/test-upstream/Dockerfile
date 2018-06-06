FROM alpine:3.2  
MAINTAINER "RideLink" https://ridelink.com  
  
# install python  
RUN apk add --update-cache python py-pip && rm -rf /var/cache/apk/*  
  
ADD requirements.txt /  
RUN pip install -r requirements.txt  
  
ADD echo.py /  
  
EXPOSE 8080  
CMD ["/usr/bin/python", "echo.py"]  

