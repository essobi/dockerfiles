# VERSION 0.1  
# AUTHOR: James Wilmot <jameswilmot2000@gmail.com>  
# DESCRIPTION: Image with MoinMoin wiki, uwsgi, nginx, self signed SSL and
memodump theme  
# TO_BUILD: docker build -t moinmoin-personalwiki .  
# TO_RUN: docker run -it -p 80:80 -p 443:443 --name my_wiki moinmoin-
personalwiki  
FROM ubuntu:trusty  
MAINTAINER James Wilmot <jameswilmot2000@gmail.com>  
  
# Set the version you want of MoinMoin  
ENV MM_VERSION 1.9.8  
# default wiki configuration  
ENV WIKI_NAME "My personal wiki"  
ENV WIKI_ADMIN "admin"  
ENV WIKI_FRONTPAGE "FrontPage"  
ENV WIKI_THEME "memodump"  
#ENV MM_CSUM 4a616d12a03f51787ac996392f9279d0398bfb3b  
# Update  
RUN apt-get update -qq && apt-get -qqy upgrade  
  
# Install software  
RUN apt-get -qqy install python wget nginx uwsgi uwsgi-plugin-python rsyslog  
RUN apt-get -qqy install apache2-utils  
RUN apt-get -qqy install sed  
RUN apt-get clean  
  
# add init script  
ADD init_script.sh /usr/local/bin/  
  
# Download MoinMoin  
RUN wget \  
https://bitbucket.org/thomaswaldmann/moin-1.9/get/$MM_VERSION.tar.gz  
#RUN if [ "$MM_CSUM" != "$(shasum $MM_VERSION.tar.gz | awk '{print($1)}')" ];\  
#then exit 1; fi;  
RUN mkdir moinmoin  
RUN tar xf $MM_VERSION.tar.gz -C moinmoin --strip-components=1  
RUN rm $MM_VERSION.tar.gz  
  
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
  
# Install moinmoin-memodump theme  
ADD memodump.py /usr/local/share/moin/data/plugin/theme/  
ADD memodump/ /usr/local/lib/python2.7/dist-
packages/MoinMoin/web/static/htdocs/memodump  
RUN chown -R www-data:www-data /usr/local/share/moin/data  
  
# Configure nginx  
ADD nginx.conf /etc/nginx/  
ADD moinmoin.conf /etc/nginx/sites-available/  
RUN mkdir -p /var/cache/nginx/cache  
RUN ln -s /etc/nginx/sites-available/moinmoin.conf \  
/etc/nginx/sites-enabled/moinmoin.conf  
RUN rm /etc/nginx/sites-enabled/default  
  
# Create self signed certificate  
ADD generate_ssl_key.sh /usr/local/bin/  
RUN /usr/local/bin/generate_ssl_key.sh moinmoin.example.org  
RUN mv cert.pem /etc/ssl/certs/  
RUN mv key.pem /etc/ssl/private/  
  
VOLUME /usr/local/share/moin/data  
  
EXPOSE 80  
EXPOSE 443  
CMD bash -C '/usr/local/bin/init_script.sh'; \  
service rsyslog start && service nginx start && \  
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

