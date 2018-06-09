FROM php:7.0-apache  
  
  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load  
  
RUN apt-get update -y  
RUN apt-get install -y build-essential  
RUN apt-get install -y nodejs  
RUN apt-get install -y ruby-full  
RUN apt-get install -y npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN gem install --no-rdoc --no-ri sass -v 3.4.22  
RUN gem install --no-rdoc --no-ri compass  
  
RUN npm install -g grunt-cli  
  
COPY . /var/www/html/  
WORKDIR /var/www/html/  
  
RUN npm install  
  
RUN grunt  

