FROM nginx:1.7.10  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
python python-pip python-dev\  
build-essential \  
supervisor \  
python-numpy \  
&& apt-get clean  
  
RUN pip install cloudant uwsgi  
  
RUN mkdir -p /home/uwsgi \  
&& mkdir -p /etc/uwsgi/vassals \  
&& mkdir /database_attachments  
  
VOLUME [ "/var/log/supervisor", "/database_attachments" ]  
  
COPY ./nginx.conf /etc/nginx/nginx.conf  
COPY ./build-conf-files.py /build-conf-files.py  
COPY ./nginx-base.conf.in /nginx-base.conf.in  
COPY ./nginx-auth.conf.in /nginx-auth.conf.in  
COPY ./docker-entrypoint.sh /entrypoint.sh  
COPY ./wsgi.ini /etc/uwsgi/vassals/wsgi.ini  
COPY ./handle_req.py /home/uwsgi/handle_req.py  
COPY ./supervisor-app.conf /etc/supervisor/conf.d/supervisor-app.conf  
  
EXPOSE 80  
EXPOSE 5984  
# The folloing only for docker connections!  
EXPOSE 5983  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx"]  

