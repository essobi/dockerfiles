FROM canercandan/nginx_passenger_python2-base  
MAINTAINER Caner Candan <caner@candan.fr>  
  
# Set the version you want of MoinMoin  
ENV MM_VERSION 1.9.7  
ENV MM_CSUM 38b7783abb8530253545d780c8019721  
  
WORKDIR /root  
  
# Download MoinMoin  
RUN wget \  
https://bitbucket.org/thomaswaldmann/moin-1.9/get/$MM_VERSION.tar.gz  
RUN if [ "$MM_CSUM" != "$(md5sum $MM_VERSION.tar.gz | awk '{print($1)}')" ];\  
then exit 1; fi;  
RUN mkdir moinmoin  
RUN tar xf $MM_VERSION.tar.gz -C moinmoin --strip-components=1  
RUN rm $MM_VERSION.tar.gz  
  
# Install MoinMoin  
RUN cd moinmoin && python setup.py install --force --prefix=/usr/local  
RUN mkdir /usr/local/share/moin/conf  
ADD wikiconfig.py /usr/local/share/moin/conf/  
RUN mkdir /usr/local/share/moin/underlay  
RUN chown -R www-data:www-data /usr/local/share/moin/underlay  
# Because of a permission error with chown I change the user here  
USER www-data  
RUN cd /usr/local/share/moin/ && tar xf underlay.tar -C underlay --strip-
components=1  
USER root  
ADD logo.png /usr/local/lib/python2.7/dist-
packages/MoinMoin/web/static/htdocs/common/  
  
# Configure nginx  
ADD passenger_wsgi.py /usr/local/share/moin/  
RUN mkdir /usr/local/share/moin/public  
  
RUN rm -rf /app  
RUN ln -s /usr/local/share/moin /app  
RUN ln -s /usr/local/share/moin/conf/wikiconfig.py
/usr/local/share/moin/wikiconfig.py  
RUN chown -R www-data:www-data /usr/local/share/moin  
  
VOLUME /usr/local/share/moin/data  
VOLUME /usr/local/share/moin/conf  
  
EXPOSE 80  
CMD [ "nginx" ]  

