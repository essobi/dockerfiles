FROM gucluozturk/python-nginx-uwsgi  
  
maintainer gucluozturk <gucluozturk@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN mkdir -p /var/log/uwsgi  
RUN chown www-data /var/log/uwsgi  
RUN chgrp www-data /var/log/uwsgi  
RUN mkdir -p /var/www  
RUN rm -rf /var/www/*  
RUN git clone https://github.com/gucluoz/mqtt-rest /var/www/mqtt-rest  
RUN pip install -r /var/www/mqtt-rest/requirements.txt  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
COPY nginx.conf /etc/nginx/sites-enabled/  
RUN mkdir -p /etc/uwsgi/vassals  
COPY uwsgi.ini /etc/uwsgi/vassals/  
COPY uwsgi_params /var/www/mqtt-rest/  
RUN cd /var/www/mqtt-rest && python /var/www/mqtt-rest/manage.py db upgrade  
  
EXPOSE 80  
CMD sh -c "uwsgi --emperor /etc/uwsgi/vassals --daemonize
/var/log/uwsgi/uwsgi.log && service nginx start"

