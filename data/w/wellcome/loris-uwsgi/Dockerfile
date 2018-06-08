FROM alpine  
  
LABEL maintainer="a.chan@wellcome.ac.uk"  
LABEL description="A Docker image running the Loris IIIF Image server"  
  
COPY install_loris.sh /install_loris.sh  
RUN /install_loris.sh  
  
# Install dependencies for UWSGI.  
RUN apk update && apk add uwsgi uwsgi-python && rm -rf /var/cache/apk/*  
  
# Copy in other config files  
COPY loris2.wsgi /var/www/loris2/loris2.wsgi  
COPY loris2.conf /opt/loris/etc/loris2.conf  
COPY uwsgi.ini /etc/uwsgi  
  
EXPOSE 8888  
CMD ["/usr/sbin/uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini", "--enable-threads"]  

