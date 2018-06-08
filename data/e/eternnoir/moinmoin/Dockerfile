#  
# Ubuntu 14.04 with moinmoinWiki Dockerfile  
#  
# Pull base image.  
FROM eternnoir/ubuntu-14.04-sshd  
MAINTAINER Frank Wang "eternnoir@gmail.com"  
ENV MOIN_VERSION 1.9.8  
#Update  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install python wget nginx uwsgi uwsgi-plugin-python rsyslog  
RUN apt-get clean  
  
RUN wget
https://bitbucket.org/thomaswaldmann/moin-1.9/get/$MOIN_VERSION.tar.gz  
RUN mkdir moinmoin  
RUN tar xf $MOIN_VERSION.tar.gz -C moinmoin --strip-components=1  
RUN rm $MOIN_VERSION.tar.gz  
  
# Install MoinMoin  
RUN cd moinmoin && python setup.py install --force --prefix=/usr/local  
ADD wikiconfig.py /usr/local/share/moin/  
RUN mkdir /usr/local/share/moin/underlay  
RUN chown -Rh www-data:www-data /usr/local/share/moin/underlay  
# Because of a permission error with chown I change the user here  
USER www-data  
RUN cd /usr/local/share/moin/ && tar xf underlay.tar -C underlay --strip-
components=1  
USER root  
RUN chown -R www-data:www-data /usr/local/share/moin/data  
ADD logo.png /usr/local/lib/python2.7/dist-
packages/MoinMoin/web/static/htdocs/common/  
  
# Configure nginx  
ADD nginx.conf /etc/nginx/  
ADD moinmoin.conf /etc/nginx/sites-available/  
RUN mkdir -p /var/cache/nginx/cache  
RUN ln -s /etc/nginx/sites-available/moinmoin.conf \  
/etc/nginx/sites-enabled/moinmoin.conf  
RUN rm /etc/nginx/sites-enabled/default  
  
VOLUME /usr/local/share/moin  
  
EXPOSE 80  
CMD service rsyslog start && service nginx start && \  
uwsgi --uid www-data \  
-s /tmp/uwsgi.sock \  
\--plugins python \  
\--pidfile /var/run/uwsgi-moinmoin.pid \  
\--wsgi-file server/moin.wsgi \  
-M -p 4 \  
\--chdir /usr/local/share/moin \  
\--python-path /usr/local/share/moin \  
\--harakiri 30 \  
\--die-on-term  

