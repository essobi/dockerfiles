FROM phusion/baseimage:0.9.19  
MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>  
  
ENV CKAN_VERSION release-v2.6-latest  
  
ENV HOME /root  
ENV CKAN_HOME /usr/lib/ckan/default  
ENV CKAN_CONFIG /etc/ckan/default  
ENV CKAN_DATA /var/lib/ckan  
  
# Install required packages  
RUN apt-get -q -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install \  
python-minimal \  
python-dev \  
python-virtualenv \  
libevent-dev \  
libpq-dev \  
nginx-light \  
apache2 \  
libapache2-mod-wsgi \  
postfix \  
build-essential \  
git  
  
# Install CKAN  
RUN virtualenv $CKAN_HOME  
RUN mkdir -p $CKAN_HOME $CKAN_CONFIG $CKAN_DATA  
RUN chown www-data:www-data $CKAN_DATA  
  
RUN git clone https://github.com/ckan/ckan $CKAN_HOME/src/ckan  
WORKDIR $CKAN_HOME/src/ckan  
RUN git checkout $CKAN_VERSION  
  
#Install dependencies  
RUN $CKAN_HOME/bin/pip install -r $CKAN_HOME/src/ckan/requirements.txt  
RUN $CKAN_HOME/bin/pip install -e $CKAN_HOME/src/ckan/  
  
#Copy config files  
RUN ln -s $CKAN_HOME/src/ckan/ckan/config/who.ini $CKAN_CONFIG/who.ini  
RUN cp $CKAN_HOME/src/ckan/contrib/docker/apache.wsgi $CKAN_CONFIG/apache.wsgi  
  
# Configure apache  
RUN cp $CKAN_HOME/src/ckan/contrib/docker/apache.conf /etc/apache2/sites-
available/ckan_default.conf  
RUN echo "Listen 8080" > /etc/apache2/ports.conf  
RUN a2ensite ckan_default  
RUN a2dissite 000-default  
  
# Configure nginx  
RUN cp $CKAN_HOME/src/ckan/contrib/docker/nginx.conf /etc/nginx/nginx.conf  
RUN mkdir /var/cache/nginx  
  
# Configure postfix  
RUN cp $CKAN_HOME/src/ckan/contrib/docker/main.cf /etc/postfix/main.cf  
  
# Configure runit  
COPY 50_configure $CKAN_HOME/src/ckan/contrib/docker/my_init.d/50_configure  
RUN cp -r $CKAN_HOME/src/ckan/contrib/docker/my_init.d/* /etc/my_init.d  
RUN cp -r $CKAN_HOME/src/ckan/contrib/docker/svc/* /etc/service  
CMD ["/sbin/my_init"]  
  
# Volumes  
VOLUME ["/etc/ckan/default"]  
VOLUME ["/var/lib/ckan"]  
EXPOSE 80  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

