#Dockerfile modern-paste  
FROM tlnk/ubuntu:latest  
MAINTAINER tlnk <support@tlnk.fr>  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
EXPOSE 80  
#Install packages  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository -y ppa:fkrull/deadsnakes && \  
apt-get update && \  
apt-get install -y \  
git \  
make \  
python3.5 \  
default-jre \  
build-essential \  
python-dev \  
libmysqlclient-dev \  
rubygems \  
python-pip \  
npm \  
apache2 \  
libapache2-mod-wsgi \  
nodejs-legacy \  
ruby-all-dev  
  
COPY entrypoint /entrypoint  
COPY modernpaste.conf /etc/apache2/sites-available/000-default.conf  
  
RUN git clone https://github.com/LINKIWI/modern-paste /var/www/modern-paste &&
\  
git config --global url."https://".insteadOf git:// && \  
chown -R www-data:www-data /var/www/modern-paste && \  
a2enmod rewrite && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/apache2/sites-
available/default-ssl.conf && \  
rm -rf /var/www/html && \  
chmod +x /entrypoint/*sh && \  
chmod +x /entrypoint/entrypoint.d/*.sh  
  
COPY flaskKey.py /var/www/modern-paste/flaskKey.py  
WORKDIR /var/www/modern-paste  
  
ENTRYPOINT ["/bin/bash", "/entrypoint/entrypoint.sh"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/tle06/modern-paste.git"  
LABEL org.label-schema.name="modern-paste"  
LABEL org.label-schema.vendor="modern-paste"  
LABEL org.label-schema.schema-version="1.0"

