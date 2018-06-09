FROM ikkyotech/nodejs_build_server:latest  
MAINTAINER "Martin Heidegger" <mh@ikkyotech.com>  
  
# Install the latest strider version  
RUN npm install -g git+https://github.com/Strider-CD/strider.git#master  
  
RUN apt-get install dialog  
  
# copy the supervisor config and the strider start script used by it  
RUN cp "$(npm root -g)/strider/docker/supervisord.conf"
/etc/supervisor/conf.d/supervisord.conf  
RUN cp "$(npm root -g)/strider/docker/start-strider.sh" /usr/local/bin/start-
strider.sh  
  
# create strider user  
RUN useradd -m strider  
  
# change the root and strider password so we can login via ssh  
# Root access is prohibited by default through ssh. To get root access login
as strider and su to root.  
RUN echo 'strider:str!der' | chpasswd  
RUN echo 'root:str!der' | chpasswd  
  
# create some directories for the database, ssh, and supervisor logs  
RUN mkdir -p /data/db && chown -R strider /data  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /var/run/sshd  
  
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 3000  

