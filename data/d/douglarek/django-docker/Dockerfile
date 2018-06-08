FROM python:3.4.3  
MAINTAINER Lingchao Xin "douglarek@gmail.com"  
# install deps from remote url, you can change it to your own.  
RUN pip install --no-cache-dir -r
https://bitbucket.org/api/2.0/snippets/douglarek/d5GL/e54f16875dd270f0dce18fe79136b845458279aa/files/django-
docker  
  
RUN apt-get update && apt-get install -y libgeos-dev && rm -rf
/var/lib/apt/lists/*  
  
# create and add needed files.  
RUN mkdir -p /opt/apps /var/log/uwsgi  
ADD .docker/uwsgi.ini /etc/uwsgi/uwsgi.ini  
RUN touch /etc/uwsgi/reload  
  
EXPOSE 8000  
CMD ["sh", "-c", "uwsgi --ini /etc/uwsgi/uwsgi.ini"]  

