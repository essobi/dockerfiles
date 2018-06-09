FROM node:8  
WORKDIR /var/app  
RUN mkdir -p /var/app  
COPY . /var/app  
  
ENV ADAPTER slack  
  
RUN apt-get update && apt-get install python-pip python-dev build-essential
supervisor zip -y  
  
RUN pip install --upgrade pip  
RUN pip install --upgrade awscli  
  
RUN npm install  
RUN npm install -g coffee-script  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
ADD contrib/startservices.sh /usr/bin/startservices.sh  
RUN chmod +x /usr/bin/startservices.sh  
  
ADD contrib/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD supervisord -c /etc/supervisor/supervisord.conf  

