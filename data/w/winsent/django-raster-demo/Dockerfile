FROM skyeer/gdal:daily  
MAINTAINER pipetc@gmail.com  
  
  
RUN apt-get -yq update && \  
apt-get -yqq install \  
git \  
ssh \  
nginx \  
supervisor \  
python3-dev \  
python-virtualenv  
  
ENV work_dir /app  
  
WORKDIR ${work_dir}  
  
ADD . .  
  
RUN virtualenv --python=python3 /env  
  
RUN /env/bin/pip install numpy uwsgi==2.0.15  
  
RUN cp ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf && \  
cp ./docker/nginx.conf /etc/nginx/sites-available/default && \  
/env/bin/pip install --upgrade -r requirements.txt  
  
RUN /env/bin/python /app/manage.py collectstatic --noinput  
  
VOLUME /env/www/media  
  
EXPOSE 80  
# set default locale for python  
ENV LANG C.UTF-8  
CMD ./docker/docker_start.sh

