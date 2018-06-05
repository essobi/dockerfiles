FROM java:8  
MAINTAINER tekHedd <tekhedd@byteheaven.net>  
  
# Force UTF-8 locale so file names on the mp3 shares will  
# make sense.  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8  
# Get ameinias from the official download at tekhedd.com:  
RUN cd /usr/local \  
&& curl -SLs http://tekhedd.com/?ddownload=2061 -o /tmp/ameinias.zip \  
&& unzip /tmp/ameinias.zip \  
&& mv ameinias-3.0.4 ameinias \  
&& rm /tmp/ameinias.zip \  
&& mkdir /adata \  
&& mkdir /mp3 \  
&& chmod 0755 ameinias/docker/bootstrap.sh  
  
# If you don't mount an MP3 dir, you'll be disappointed  
VOLUME [ "/adata", "/mp3" ]  
  
EXPOSE 7076  
WORKDIR /usr/local/ameinias  
CMD [ "/usr/local/ameinias/docker/bootstrap.sh", "ameinias" ]  

