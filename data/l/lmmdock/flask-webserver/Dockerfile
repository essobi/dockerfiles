FROM python:3.5  
# create non-root user  
RUN adduser --disabled-password --gecos '' uwsgi  
  
# setup uWSGI  
RUN pip install uwsgi  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys ABF5BD827BD9BF62
\  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y ca-certificates nginx gettext-base supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gpasswd -a uwsgi www-data  
RUN gpasswd -a nginx www-data  
  
RUN chown -R nginx /var/log/nginx /var/cache/nginx/ \  
&& touch /var/run/nginx.pid \  
&& chown -R nginx /var/run/nginx.pid \  
&& mkdir /var/run/uwsgi && touch /var/run/uwsgi/socket.sock \  
&& chown -R uwsgi:www-data /var/run/uwsgi/socket.sock \  
&& chmod g+rwx /var/run/uwsgi/socket.sock \  
&& chown -R uwsgi:www-data /var/run/uwsgi  
  
EXPOSE 8080  
# make NGINX run in foreground  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
# update NGINX config  
RUN rm /etc/nginx/conf.d/default.conf  
# copy the modified Nginx conf  
COPY docker-config/nginx.conf /etc/nginx/conf.d/  
# copy uWSGI ini file to enable default dynamic uwsgi process number  
COPY docker-config/uwsgi.ini /etc/uwsgi/  
  
# custom Supervisord config  
COPY docker-config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY docker-config/supervisord-kill.py /usr/bin/  
  
CMD ["/usr/bin/supervisord"]  
  
WORKDIR /app  

