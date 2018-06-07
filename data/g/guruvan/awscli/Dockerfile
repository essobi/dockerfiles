# To build: docker build -t <namespace>/awscli .  
# To run: docker run -it <namespace>/awscli  
# cd /apps; aws s3 command  
#FROM dockerfile/python  
FROM python:2.7  
MAINTAINER Rob Nelson <guruvan@maza.club>  
  
RUN pip install awscli s3cmd  
  
VOLUME ["/apps","/data"]  
COPY . /  
ENTRYPOINT ["/app/start.sh"]  
CMD [""]  

