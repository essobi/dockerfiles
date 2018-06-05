FROM python:2.7.11-alpine  
  
RUN apk update && apk add swig g++ openssl-dev && mkdir /Avocado  
COPY ./requirements.txt /Avocado  
WORKDIR /Avocado  
RUN pip install -r requirements.txt && rm -rf /var/cache/apk/*  
COPY ./ /Avocado  
  
EXPOSE 5000  
CMD ["python", "avocado.py"]

