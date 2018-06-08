FROM ubuntu:14.04  
MAINTAINER Jason Corbett  
  
# Other repositories  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe"
>/etc/apt/sources.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' >/etc/apt/sources.list.d/mongodb.list  
  
# Install  
RUN apt-get update  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -fs /bin/true /sbin/initctl  
RUN apt-get -y dist-upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mongodb-org python-dev
build-essential uwsgi uwsgi-plugin-python nginx-full supervisor git rabbitmq-
server librabbitmq-dev pwgen wget libxml2-dev libxslt1-dev zlib1g-dev libffi-
dev nodejs npm python3-cairo python3-cairosvg python3-dev libyaml-dev  
  
#Setup RabbitMQ  
RUN rabbitmq-plugins enable rabbitmq_management  
  
# get needed python files  
RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O -
| python3  
RUN easy_install pip  
RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O -
| python2  
RUN easy_install-2.7 pip  
RUN pip2.7 install virtualenv  
RUN pip2.7 install watchdog  
  
# setup supervisor  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD sleepandrun /usr/bin/sleepandrun  
  
# setup slick files related to starting up  
RUN mkdir -p /var/lib/slick  
ADD slick_first_init.sh /etc/slick_first_init.sh  
ADD run.sh /etc/run.sh  
ADD uwsgi.ini /var/lib/slick/uwsgi.ini  
ADD settings.cfg /var/lib/slick/settings.cfg  
ADD initmongo /var/lib/slick/initmongo  
ADD amqpconfig.js /var/lib/slick/amqpconfig.js  
ADD narc.conf /etc/narc.conf  
ADD reload.sh /var/lib/slick/reload.sh  
  
# setup nginx  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
ADD nginx.conf /etc/nginx/sites-available/slick  
RUN ln -s /etc/nginx/sites-available/slick /etc/nginx/sites-enabled/slick  
  
# install lessc  
RUN npm install -g less  
RUN ln -s /usr/bin/nodejs /usr/local/bin/node  
  
# expose our volumes  
RUN mkdir -p /data/db  
RUN mkdir -p /slick  
VOLUME ["/data", "/slick" ]  
  
# expose web, mongodb, rabbitmq, rabbitmq-management  
EXPOSE 80 27017 5672 15672  
# our custom init  
ENTRYPOINT /etc/run.sh  

