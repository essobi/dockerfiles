FROM python:2.7  
MAINTAINER Miguel Matul "miguel@pixela.com.gt"  
# Update aptitude with new repo  
RUN apt-get update  
  
# Install software  
RUN apt-get install -y git  
  
ADD . /application/  
  
RUN mkdir logs  
  
# Install Node.js  
RUN cd /tmp  
  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
  
RUN apt-get autoremove -y  
  
RUN apt-get install nodejs -y  
  
RUN apt-get install build-essential libpq-dev -y  
  
RUN npm install -g npm@latest-2  
  
RUN npm install -g bower  
  
WORKDIR /application/  
  
RUN npm install  
  
RUN bower install --allow-root  
  
RUN mkdir media static logs  
  
#RUN npm install gulp-imagemin  
RUN pip install -r requirements/PRODUCTION  
  
RUN npm install -g gulp  
  
EXPOSE 8000

