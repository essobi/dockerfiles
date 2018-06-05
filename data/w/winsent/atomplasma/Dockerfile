FROM ubuntu:14.04  
MAINTAINER pipetc@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y \  
supervisor \  
nginx \  
curl \  
mercurial \  
git \  
libpq-dev \  
python-dev \  
libjpeg-dev \  
python-virtualenv  
  
# Add RSA key  
COPY ./docker/id_rsa /root/.ssh/id_rsa  
RUN chmod 600 /root/.ssh/id_rsa  
RUN ssh-keyscan -t rsa bitbucket.org >> /root/.ssh/known_hosts  
  
ENV work_dir /app  
WORKDIR ${work_dir}  
  
RUN virtualenv /env  
  
RUN /env/bin/pip install uwsgi  
  
COPY ./requirements.txt requirements.txt  
RUN /env/bin/pip install -U -r requirements.txt  
  
COPY ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf  
  
ADD . .  
  
RUN /env/bin/python /app/manage.py collectstatic --noinput  
  
VOLUME /env/www/media  
  
EXPOSE 80  
# set default locale for python  
ENV LANG C.UTF-8  
RUN chmod +x ./docker/docker_start.sh  
CMD ./docker/docker_start.sh  

