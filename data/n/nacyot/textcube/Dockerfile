FROM tutum/apache-php  
MAINTAINER nacyot<propellerheaven@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y wget  
  
# Install Textcube  
WORKDIR /opt  
RUN wget https://github.com/Needlworks/Textcube/archive/v1.10.7.tar.gz && \  
tar xvf v1.10.7.tar.gz && \  
rm -rf /app && \  
mv Textcube-1.10.7 /app/  
RUN \  
chmod 0777 /app /app/skin/blog &&\  
chmod 0755 /app  
  
ADD ./files/apache2.conf /etc/apache2/apache2.conf  
ADD ./files/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN a2enmod rewrite  

