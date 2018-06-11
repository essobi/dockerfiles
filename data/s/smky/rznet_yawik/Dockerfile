#Download base image yawik/yawik  
FROM yawik/yawik  
  
MAINTAINER Samak Yodjunda  
  
#Install mongdb  
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
#RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
#RUN apt-get update && apt-get install -y mongodb-org  
#COPY ./config_files/mongod /etc/init.d/  
#RUN /etc/init.d/mongod start  
#Install Sendmail  
RUN apt-get update && apt-get upgrade -y sendmail && rm -rf
/var/lib/apt/lists/*  
  
COPY ./config_files/sendmail.cf /etc/mail/sendmail.cf  
COPY ./config_files/php.ini /usr/local/etc/php/php.ini  
COPY ./config_files/yawik-site.conf /etc/apache2/sites-available/yawik-
site.conf  
  
#Start send mail service  
COPY ./config_files/mail_config.sh /mail_config.sh  
RUN chmod +x /mail_config.sh  
#CMD ./mail_config.sh  

