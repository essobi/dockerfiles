FROM quirky/ruby  
MAINTAINER Micah Martin <micahlmartin@gmail.com>  
  
# Bundler  
RUN gem install bundler --version=1.3.5  
  
# Rails  
RUN gem install rails --version=3.2.18 -f  
  
# scss-lint  
RUN gem install scss-lint  
  
# Latest Nodejs  
RUN apt-add-repository ppa:chris-lea/node.js -y && \  
apt-get update -y && \  
apt-get install nodejs -y  
  
# Nodejs tools  
RUN npm install -g bower  
RUN npm install -g grunt-cli  
RUN npm install -g gulp  
  
# PostgreSQL client  
RUN apt-get install libpq-dev -y  
RUN apt-get install postgresql-client -y  
  
# Mysql client  
RUN apt-get install mysql-client libmysqlclient-dev -y  
  
# Imagemagick  
RUN apt-get install imagemagick -y  
  
ENTRYPOINT ["/sbin/my_init", "--"]  
CMD ["/bin/bash"]  

