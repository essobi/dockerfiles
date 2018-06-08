FROM alpine:3.3  
MAINTAINER "RideLink" https://ridelink.com  
  
# install python  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
rm -r /root/.cache  
  
ADD requirements.txt /  
RUN pip install -r requirements.txt  
  
EXPOSE 8080  
CMD ["moto_server", "sqs", "-p8080"]  

