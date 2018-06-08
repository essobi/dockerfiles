FROM node:9 as builder  
  
MAINTAINER cmoesgaard  
  
WORKDIR /app  
  
ADD .bowerrc *.js *.json /app/  
RUN ["npm", "install"]  
  
ADD mora/static /app/mora/static  
RUN ["npm", "run", "grunt"]  
  
# TODO: use tbeadle/gunicorn-nginx:3.5?  
FROM python:3.6-slim  
  
WORKDIR /app  
  
COPY \--from=builder /app/mora/static mora/static  
  
ADD requirements.txt /app  
RUN ["pip", "install", "-r", "requirements.txt"]  
RUN ["pip", "install", "gunicorn"]  
  
ADD . /app  
  
EXPOSE 5000  
ENV MORA_LORA_URL=http://mox:5000/  
  
CMD ["gunicorn", "--worker-class=gevent", "--workers=4", "--enable-stdio-
inheritance", "--access-logfile", "-", "--bind", "[::]:5000", "mora.app:app"]  

