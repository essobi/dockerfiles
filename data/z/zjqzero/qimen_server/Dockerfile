FROM alpine:latest  
  
MAINTAINER zhoujunqian <zjqzero@gmail.com>  
  
RUN apk update  
RUN apk add python py-pip  
RUN pip install SQLAlchemy xmltodict jsoncompare requests  
COPY ./*.* /var/app/  
RUN rm -rf /var/cache/apk/*  
  
ENV PYTHONPATH /var/app  
  
WORKDIR /var/app  
  
EXPOSE 8080  
CMD ["python", "test_server.py"]  

