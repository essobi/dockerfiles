FROM python:alpine3.6  
# Update packages  
RUN apk add --update build-base jpeg-dev zlib-dev git redis  
ENV LIBRARY_PATH=/lib:/usr/lib  
  
# Add and install Python modules  
ADD requirements.txt /src/requirements.txt  
RUN cd /src; pip install -r requirements.txt  
  
# Bundle app source  
ADD . /src  
WORKDIR /src  
  
EXPOSE 5000  
CMD ["honcho", "start"]  

