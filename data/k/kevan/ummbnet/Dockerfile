FROM nginx:1.9  
RUN \  
apt-get update && apt-get install -y --no-install-recommends \  
python-software-properties=0.92.25debian1 \  
python-setuptools=5.5.1-1 \  
build-essential=11.7 \  
supervisor=3.0r1-1 \  
python-dev=2.7.9-1 \  
python=2.7.9-1 \  
libpq-dev=9.4.1-1  
  
RUN mkdir -p /var/log/supervisor  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN easy_install pip  
RUN pip install uwsgi  
  
# Allow requirements to be cached  
COPY requirements.txt /home/docker/code/  
RUN pip install -r /home/docker/code/requirements.txt  
  
COPY . /home/docker/code/  
  
RUN rm /etc/nginx/conf.d/default.conf  
RUN ln -s /home/docker/code/default.conf /etc/nginx/conf.d/  
RUN ln -s /home/docker/code/supervisord.conf /etc/supervisor/conf.d/  
  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

