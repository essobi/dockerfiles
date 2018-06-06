FROM phusion/baseimage:0.9.16  
MAINTAINER pinion <pinion@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
# install dependencies for building cherrymusic  
#jon-severinsson's repo quit working for me :(  
#RUN add-apt-repository ppa:jon-severinsson/ffmpeg  
RUN apt-add-repository ppa:mc3man/trusty-media  
RUN apt-get update -qq  
RUN apt-get -y install ffmpeg python3-cherrypy3 imagemagick python-unidecode
git mpg123 faad vorbis-tools flac imagemagick python-pip lame libmp3lame0  
RUN apt-get clean  
RUN pip install cherrypy  
  
# download and install cherrymusic  
RUN git clone \--branch master https://github.com/devsnd/cherrymusic.git
/opt/cherrymusic  
RUN chown nobody:users /opt/cherrymusic  
RUN mkdir -p ~/.config/cherrymusic  
  
EXPOSE 8070  
# cherrymusic Configuration  
VOLUME ~/.config/cherrymusic/  
  
# Music directory  
VOLUME /music  
  
# Add cherrymusic to runit  
RUN mkdir /etc/service/cherrymusic  
ADD cherrymusic.sh /etc/service/cherrymusic/run  
RUN chmod +x /etc/service/cherrymusic/run  

