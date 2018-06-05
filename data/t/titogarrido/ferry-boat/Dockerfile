FROM titogarrido/web2py-nginx-uwsgi-nossl  
  
MAINTAINER Tito Garrido <titogarrido@gmail.com>  
  
RUN pip install celery docker-py psutil  
  
RUN apt-get update  
  
RUN apt-get install -y git  
  
RUN mkdir /home/www-data/web2py/applications/ferry_boat  
  
RUN git clone https://github.com/Titosoft/ferry-boat.git /tmp/ferry-boat  
  
RUN cp -r /tmp/ferry-boat/web2py/applications/ferry_boat/* /home/www-
data/web2py/applications/ferry_boat  
RUN cp /tmp/ferry-boat/web2py/routes.py /home/www-data/web2py/routes.py  
  
RUN chown -R www-data:www-data /home/www-data/web2py/  
RUN sed -i 's/user www-data/user root/g' /etc/nginx/nginx.conf  
RUN sed -i 's/uid = www-data/uid = root/g' /etc/uwsgi/web2py.ini  
  
RUN mkdir /var/log/ferry-btm/  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /etc/service/celery  
ADD celery_init /etc/service/celery/run  
RUN chmod 755 /etc/service/celery/run  
  
EXPOSE 80  
WORKDIR /home/www-data/web2py  
  
CMD /etc/service/celery/run  
  
CMD ["/sbin/my_init"]  

