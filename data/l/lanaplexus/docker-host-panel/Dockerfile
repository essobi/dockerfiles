FROM phusion/passenger-full:0.9.15  
ENV HOME /home/app  
  
CMD ["/sbin/my_init"]  
  
RUN sed -i "/^# deb.*backports/ s/^# //" /etc/apt/sources.list  
  
RUN apt-get -qq update  
#RUN apt-get -y upgrade  
RUN apt-get install -y wget htop psmisc mc daemontools curl lynx  
RUN locale-gen en_US  
RUN locale-gen en_US.UTF-8  
RUN locale-gen uk_UA  
RUN locale-gen uk_UA.UTF-8  
RUN locale-gen ru_RU  
RUN locale-gen ru_RU.UTF-8  
RUN update-locale LC_ALL=uk_UA.UTF-8 LANG=uk_UA.UTF-8  
  
# Install Python 3.4  
RUN apt-get -y install python3.4 python3-pip python3.4-dev libpq-dev libjpeg-
dev libfreetype6-dev zlib1g-dev  
RUN apt-get -y build-dep python3-pil  
RUN apt-get -y install libxml2-dev apache2-utils  
  
RUN ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/  
RUN ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/  
RUN ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/  
RUN cd /usr/include  
RUN ln -s freetype2 freetype  
  
RUN alias python="python3"  
ADD .bash_aliases /home/app/.bash_aliases  
ADD .bash_aliases /root/.bash_aliases  
  
RUN git clone -b beta https://korkholeh@bitbucket.org/korkholeh/sbits-host-
panel.git /home/app/webapp  
  
RUN mkdir /home/app/webapp/public  
RUN mkdir /home/app/webapp/tmp  
RUN touch /home/app/webapp/tmp/restart.txt  
  
RUN easy_install3 -U pip  
RUN pip3 install -r /home/app/webapp/requirements/production.txt  
RUN pip3 install python3-memcached  
  
ADD passenger_wsgi.py /home/app/webapp/passenger_wsgi.py  
  
RUN python3 /home/app/webapp/host_panel/manage.py collectstatic --noinput
--settings=host_panel.settings.production  
  
# Enable Nginx and Passenger  
RUN rm -f /etc/service/nginx/down  
ADD webapp.conf /etc/nginx/sites-enabled/webapp.conf  
  
# Enable SSH  
RUN rm -f /etc/service/sshd/down  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Enable the Redis service.  
RUN rm -f /etc/service/redis/down  
  
# Enable the memcached service.  
RUN rm -f /etc/service/memcached/down  
  
VOLUME /var/log  
VOLUME /home/app  
VOLUME /etc/nginx/sites-enabled  
  
RUN echo -n uk_UA.UTF-8 > /etc/container_environment/LANG  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  

