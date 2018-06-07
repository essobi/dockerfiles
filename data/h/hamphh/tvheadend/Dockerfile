FROM hamphh/unraidbase:latest  
  
EXPOSE 9981 9982  
VOLUME /config \  
/recordings  
  
# Add tvheadend repo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
379CE192D401AB61  
RUN echo "deb https://dl.bintray.com/tvheadend/deb xenial stable-4.2" | tee -a
/etc/apt/sources.list  
RUN apt-get update -qq  
  
# Install tvheadend  
RUN apt-get -qy install tvheadend; exit 0  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add tv_grab_wg to /usr/bin/  
ADD tv_grab_wg tv_grab_file /usr/bin/  
RUN chmod +x /usr/bin/tv_grab_*  
  
#Start tvheadend when container starts  
RUN mkdir -p /etc/service/tvheadend  
ADD tvheadend.sh /etc/service/tvheadend/run  
RUN chmod +x /etc/service/tvheadend/run  

