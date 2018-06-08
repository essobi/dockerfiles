FROM debian:wheezy  
MAINTAINER Romain GOUYET "docker@gouyet.com"  
ENV REFRESHED_AT 2016-03-15  
RUN echo "deb http://www.promixis.com/repo/debian/wheezy wheezy main" >>
/etc/apt/sources.list  
RUN apt-get -y -q update  
RUN apt-get -y -q install wget  
RUN wget -O - http://www.promixis.com/repo/debian/wheezy/sales.key | apt-key
add -  
RUN apt-get -y -q upgrade  
RUN apt-get --force-yes -y -q install girder  
# Missing Girder dependencies  
RUN apt-get -y -q install libgl1-mesa-glx  
RUN apt-get -y -q install libpng12-0  
RUN apt-get -y -q install libegl1-mesa  
RUN apt-get -y -q install libglib2.0-0  
RUN apt-get -y -q install libpulse0  
# For USB devices  
RUN apt-get -y -q install usbutils  
# For modprob  
RUN apt-get -y -q install module-init-tools  
# Folder for licence  
RUN mkdir /opt/girder/qt/etc/xdg/Promixis  
# Temporary, to test Serial Device  
ADD Teleinfo/ /opt/girder/lua/teleinfo  
# For Front-end communication  
EXPOSE 20000  
# For Girder Webserver  
EXPOSE 80  
# For Extra LUA script and plugin ?  
#RUN mkdir /opt/girder/luaext  
#VOLUME /opt/girder/luaext  
# Folder for Girder Licence  
VOLUME /opt/girder/qt/etc/xdg/Promixis  
# Folder for Girder Web Server files  
VOLUME /opt/girder/httpd  
#Launch Girder 6 Service  
CMD /opt/girder/Girder6Service && tail -F /var/log/girder  

