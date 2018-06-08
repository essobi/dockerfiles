FROM nginx:stable  
  
RUN apt-get update  
RUN apt-get -y install build-essential checkinstall  
RUN apt-get -y install libssl-dev  
RUN apt-get -y install git  
RUN apt-get -y install curl  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get -y install python nodejs  
COPY nginx.conf /etc/nginx/sites-enabled/default  
  
RUN mkdir code  
WORKDIR /code  
COPY . ./  
RUN npm install  
RUN npm rebuild node-sass  
  
EXPOSE 80 443  
ENTRYPOINT ["sh", "./entrypoint.sh"]  

