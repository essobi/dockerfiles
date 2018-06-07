# start with a base image  
FROM alpine:latest  
MAINTAINER Real Python <info@realpython.com>  
  
# install dependencies  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
docker \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/*  
  
RUN pip install flask  
  
# update working directories  
ADD ./app /app  
  
CMD chmod +x app/deploy.sh  
CMD python app/app.py  

