FROM binhex/arch-base:latest
MAINTAINER binhex

# additional files
##################
# add supervisor conf file for app
ADD *.conf /etc/supervisor/conf.d/

# add bash scripts to install app
ADD install.sh /root/install.sh

# copy start bash script to subsonic dir (checks ssl enabled/disabled and copies transcoders to subsonic install dir)
ADD start.sh /opt/subsonic/start.sh

# install app
#############
# make executable and run bash scripts to install app
RUN chmod +x /root/*.sh /opt/subsonic/*.sh && /bin/bash /root/install.sh

# docker settings
#################
# set env variable for java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk/jre

# map /config to host defined config path (used to store configuration from app)
VOLUME /config

# map /media to host defined media path (used to read/write to media library)
VOLUME /media

# expose port for http
EXPOSE 4040
# expose port for https
EXPOSE 4050
# run supervisor
################
# run supervisor
CMD ["supervisord", "-c", "/etc/supervisor.conf", "-n"]
