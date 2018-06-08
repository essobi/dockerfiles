# meedan/ruby  
  
FROM meedan/nodejs  
MAINTAINER sysops@meedan.com  
  
# passenger  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7  
RUN echo deb https://oss-binaries.phusionpassenger.com/apt/passenger trusty
main > /etc/apt/sources.list.d/passenger.list  
  
# ruby 2.3 repos  
RUN apt-add-repository ppa:brightbox/ruby-ng \  
&& apt-get update --fix-missing  
  
#
http://www.modrails.com/documentation/Users%20guide%20Nginx.html#_installing_packages  
# supervisor is installed since it gets used frequently to kick off delayed
job  
# imagemagick is used by several downstream containers  
RUN apt-get install -y \  
ruby2.3 \  
ruby2.3-dev \  
ruby2.3-doc \  
build-essential \  
libv8-dev \  
libpq-dev \  
sqlite3 \  
libsqlite3-dev \  
libmysqlclient-dev \  
bcrypt \  
libicu52 \  
supervisor \  
tidy \  
nginx \  
nginx-extras \  
ruby-rack \  
passenger \  
imagemagick  
  
# work around for passenger checksum  
# nginx \  
# nginx-extras \  
# ENV PASSENGER_VERSION=5.1.11 \  
# NGINX_VERSION=1.12.1  
# ADD https://oss-
binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/p/passenger/passenger_${PASSENGER_VERSION}-1~trusty1_amd64.deb
./passenger_${PASSENGER_VERSION}-1~trusty1_amd64.deb  
# ADD https://oss-
binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-
common_${NGINX_VERSION}-8.5.1.9~trusty1_all.deb ./nginx-
common_${NGINX_VERSION}-8.5.1.9~trusty1_all.deb  
# ADD https://oss-
binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-
extras_${NGINX_VERSION}-8.5.1.9~trusty1_amd64.deb ./nginx-
extras_${NGINX_VERSION}-8.5.1.9~trusty1_amd64.deb  
# ADD https://oss-
binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx_${NGINX_VERSION}-8.5.1.9~trusty1_all.deb
./nginx_${NGINX_VERSION}-8.5.1.9~trusty1_all.deb  
  
# RUN dpkg -i ./passenger_${PASSENGER_VERSION}-1~trusty1_amd64.deb \  
# && dpkg -i ./nginx-common_${NGINX_VERSION}-8.5.1.9~trusty1_all.deb \  
# && dpkg -i ./nginx-extras_${NGINX_VERSION}-8.5.1.9~trusty1_amd64.deb \  
# && dpkg -i ./nginx_${NGINX_VERSION}-8.5.1.9~trusty1_all.deb \  
# && rm ./passenger_${PASSENGER_VERSION}-1~trusty1_amd64.deb \  
# && rm ./nginx_${NGINX_VERSION}-8.5.1.9~trusty1_all.deb \  
# && rm ./nginx-extras_${NGINX_VERSION}-8.5.1.9~trusty1_amd64.deb  
  
# ruby config  
RUN rm /usr/bin/ruby \  
&& ln -s /usr/bin/ruby2.3 /usr/bin/ruby \  
&& rm -f /usr/bin/gem \  
&& ln -s /usr/bin/gem2.3 /usr/bin/gem \  
&& rm -f /usr/bin/rake \  
&& ln -s /usr/bin/rake2.3 /usr/bin/rake  
  
# bundler  
RUN gem install bundler --no-rdoc --no-ri  
  
# irbrc  
COPY ./config/root/ /root/  
  
# nginx  
COPY ./config/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY ./config/nginx/passenger.conf /etc/nginx/conf.d/passenger.conf  
  
ONBUILD EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]

