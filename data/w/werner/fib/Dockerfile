# fib  
#  
# VERSION 1.0  
FROM ubuntu:14.04  
MAINTAINER Werner R. Mendizabal "werner.mendizabal@gmail.com"  
RUN apt-get update  
  
RUN apt-get install -y curl git-core nginx openssh-server python-pip uwsgi
uwsgi-plugin-python  
  
RUN pip install virtualenv  
  
RUN virtualenv /var/www/fib/env  
  
ADD files/run.sh /var/www/fib/run.sh  
ADD files/default /etc/nginx/sites-enabled/default  
ADD files/uwsgi.ini /etc/uwsgi/apps-enabled/uwsgi.ini  
  
RUN chown -R www-data:www-data /var/www/fib  
  
RUN sed -i s/www-data/root/ /etc/nginx/nginx.conf  
  
ADD / /var/www/fib  
  
WORKDIR /var/www/fib  
  
RUN . /var/www/fib/env/bin/activate && python setup.py install  
  
EXPOSE 80  
  
CMD ./run.sh  

