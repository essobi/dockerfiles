FROM leloupmechant/docker-starters:php5.4-apache  
  
#set ENNVIRONEMENT  
ENV env dev  
  
#env app dir  
ENV app_dir /var/www/  
  
  
#install node & build tools  
RUN apt-get update  
#install curl  
RUN apt-get install -y curl  
RUN curl --silent --location https://deb.nodesource.com/setup_0.12 | bash -  
RUN apt-get install --yes nodejs  
RUN apt-get install -y build-essential  
  
RUN apt-get update  
RUN apt-get -y upgrade  
#RUN apt-get install --yes nodejs-legacy  
RUN apt-get install -y ruby  
RUN gem install sass  
  
#install node utilities  
RUN npm install -g gulp  
RUN npm install -g grunt  
RUN npm install -g bower  
  
VOLUME ${app_dir}  
WORKDIR ${app_dir}  
  
#initialize  
#RUN npm install  
#RUN bower --config.interactive=false --allow-root install

