FROM ubuntu:trusty  
  
MAINTAINER itsnotme  
  
RUN apt-get update \  
&& apt-get install -y python python3 python3-pip nginx supervisor pkg-config \  
libfreetype6-dev python3-numpy python3-matplotlib python3-scipy \  
libhdf5-7 libhdf5-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY requirements_docker.txt /var/www/storage/requirements_docker.txt  
WORKDIR /var/www/storage/  
  
RUN pip3 install -r requirements_docker.txt  
  
COPY . /var/www/storage/  
  
RUN echo "MONGODB_URI = 'mongodb://database:27017'" > conf.py  
  
# setup nginx  
RUN mkdir -p logs && echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& rm /etc/nginx/sites-enabled/default \  
&& cp /var/www/storage/storage_nginx.conf /etc/nginx/sites-available/ \  
&& ln -s /etc/nginx/sites-available/storage_nginx.conf /etc/nginx/sites-
enabled/  
  
# setup supervisord  
# RUN mkdir -p /var/log/supervisor  
RUN cp storage_supervisord.conf /etc/supervisor/conf.d/  
  
EXPOSE 5006  
CMD ["supervisord", "-n"]

