# set base os  
FROM phusion/baseimage:0.9.17  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Configure user nobody to match unRAID's settings  
RUN \  
usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
RUN add-apt-repository ppa:fkrull/deadsnakes-python2.7 -y  
RUN apt-get update -qq  
  
# install dependencies for building mylar  
RUN apt-get install python git-core python-openssl wget unrar -qq  
RUN apt-get clean  
  
# download and install mylar  
RUN git clone https://github.com/evilhero/mylar.git -b development /opt/mylar  
  
# install comictagger  
RUN git clone https://github.com/scooterpsu/comictagger.git /opt/comictagger  
RUN cp -R /opt/comictagger/comictagger.py /opt/mylar  
RUN cp -R /opt/comictagger/comictaggerlib /opt/mylar/lib  
  
RUN chown nobody:users /opt/mylar  
  
EXPOSE 8090  
# mylar Configuration  
VOLUME /config  
  
# Downloads directory  
VOLUME /downloads  
  
# comics directory  
VOLUME /comics  
  
# Copy out the auto processing scripts to the config directory  
RUN \  
cp -R /opt/mylar/post-processing/ /config/ && \  
cp /opt/mylar/*.csv /config/  
  
#change ownership on opt because HEY! Maybe it will fix that one thing! ...?  
RUN chown -R nobody:users /opt  
  
# Add mylar to runit  
RUN mkdir /etc/service/mylar  
ADD mylar.sh /etc/service/mylar/run  
RUN chmod +x /etc/service/mylar/run  

