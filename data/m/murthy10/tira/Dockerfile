FROM django:latest  
  
MAINTAINER Samuel Kurath <skurath@hsr.ch>  
  
EXPOSE 8000  
  
RUN apt-get update \  
&& apt-get install -y nginx python-pip python-dev git vim \  
&& export
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp34-cp34m-linux_x86_64.whl
\  
&& pip install --upgrade pip \  
&& pip3 install --upgrade $TF_BINARY_URL \  
&& pip install uwsgi \  
&& pip install pillow \  
&& cd / \  
&& git clone https://github.com/Murthy10/tira.git \  
&& ln -s /tira/tira/docker/tira_nginx.conf /etc/nginx/sites-enabled/ \  
&& cd /tira/ \  
&& echo 'yes' | python manage.py collectstatic \  
&& rm db.sqlite3 \  
&& python manage.py makemigrations recognition \  
&& python manage.py migrate \  
&& chmod +x /tira/tira/docker/start.sh  
CMD ["/tira/tira/docker/start.sh"]

