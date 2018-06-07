FROM python:2.7  
MAINTAINER Person Sebastien <personseb@yahoo.fr>  
  
# no need for confirmation  
ENV DEBIAN_FRONTEND noninteractive  
  
# see http://www.garron.me/en/blog/ubuntu-deb-proxy-cache.html  
#RUN echo 'Acquire::http { Proxy "http://192.168.0.32:3142"; };' >
/etc/apt/apt.conf.d/use-local-proxy  
RUN apt-get -qq update  
  
# Recommends are as of now still abused in many packages  
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/no-recommends  
RUN echo "APT::Get::Assume-Yes "true";" > /etc/apt/apt.conf.d/always-yes  
  
RUN apt-get -y install git-core  
WORKDIR /domogik  
RUN git clone git://github.com/domogik/domogik.git /domogik  
  
# retrieve missing package dependancy  
RUN apt-get -q -y install gcc g++ \  
alembic \  
gettext \  
adduser mysql-client \  
libssl-dev libzmq-dev libpq-dev python-psycopg2 python-mako libffi-dev  
  
# update sources  
RUN git pull  
  
## first run : init all the part except db  
RUN ./install.py --command-line --user domogik \  
\--database_type mysql --database_host db_1 --database_name domogik
--database_user domogik --database_password domopass  
  
ADD domogik-init.sh /domogik-init.sh  
  
CMD ["/domogik-init.sh"]  
  
#VOLUME ["/data"]  
EXPOSE 3865 40405 40406 40410 40411 40412  

