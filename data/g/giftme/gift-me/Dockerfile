FROM node:6  
MAINTAINER Aaron Buxbaum "me@aaronbuxbaum.com"  
ENV CI true  
  
RUN apt-get update -y -qq  
RUN apt-get install -y -qq python python-dev python-pip  
  
COPY . /app  
WORKDIR /app  
  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
RUN npm install --silent  
RUN npm rebuild node-sass  
  
RUN npm run build  
CMD gunicorn hello:app --pythonpath api

