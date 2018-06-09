FROM python:3.5  
MAINTAINER Touch4IT <hi@touch4it.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
locales \  
gettext \  
ca-certificates \  
nginx \  
&& apt-get clean  
  
COPY conf/taiga /taiga  
COPY taiga-back /taiga/taiga-back  
COPY taiga-front-dist /taiga/taiga-front-dist  
  
COPY conf/nginx /etc/nginx  
  
# Link configuration files and nginx logs:  
RUN ln -sf /taiga/conf.json /taiga/taiga-front-dist/dist/conf.json; \  
ln -sf /taiga/local.py /taiga/taiga-back/settings/local.py; \  
ln -sf /taiga/celery_local.py /taiga/taiga-back/settings/celery_local.py; \  
ln -sf /dev/stdout /var/log/nginx/access.log; \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
WORKDIR /taiga/taiga-back  
  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["gunicorn", "-w 3", "-t 60", "--pythonpath=.", "-b 127.0.0.1:8000",
"taiga.wsgi"]  
  
EXPOSE 80  
VOLUME /taiga/taiga-back/media  

