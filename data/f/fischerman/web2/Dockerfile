FROM tutum/lamp  
MAINTAINER fischerman  
  
RUN apt-get update && \  
apt-get -y install nodejs npm ruby-full  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN gem install sass  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
  
WORKDIR /tmp  
  
ADD . /tmp/web2/  
  
WORKDIR /tmp/web2  
  
RUN npm install  
RUN bower install --allow-root  
  
RUN grunt build  
  
RUN rm -rf /app/*  
RUN cp -r dist/. /app  
  
RUN sed -i '19i\mysql -uroot < /tmp/web2/example/dummy.sql\'
/create_mysql_admin_user.sh  
  
RUN cp example/config.php /app/  

