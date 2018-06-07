FROM ubuntu:latest  
RUN apt-get update -y && apt-get install -y supervisor software-properties-
common vim  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN apt-get install -y oracle-java8-installer maven supervisor python-pip
python-dev build-essential postgresql-client-common libpq-dev curl libssl-dev
libcurl4-openssl-dev  
RUN apt-get install -y apache2  
  
RUN a2enmod ssl  
RUN a2enmod proxy  
RUN a2enmod proxy_http  
RUN a2enmod rewrite  
RUN a2enmod headers  
RUN mkdir /var/lock/apache2  
RUN mkdir /var/run/apache2  
  
# Copy Files over  
WORKDIR /app  
COPY . /app  
  
# Install the SSH endpoint  
RUN cd /app/endpoints/ssh && mvn assembly:assembly  
COPY env/supervisor-app.conf /etc/supervisor/conf.d/  
COPY env/couchdrop-apache-lb.conf /etc/apache2/sites-enabled/  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
  
# Install the UWSGI applications  
RUN pip install uwsgi  
RUN pip install -r service/requirements.txt  
RUN pip install -r web/requirements.txt  
  
EXPOSE 5022 80 443  
CMD ["supervisord", "-n"]  
  

