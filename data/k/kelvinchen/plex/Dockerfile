FROM kelvinchen/base:latest  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends wget udev \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone \--depth=1 "https://github.com/mrworf/plexupdate.git"
/opt/plexupdate  
  
ENV PATH="${PATH}:/opt/plexupdate"  
VOLUME /config  
  
EXPOSE 32400/tcp 1900/udp 3005/tcp 5353/udp 8324/tcp 32410-32414/udp 32469/tcp  
  
COPY container-root/ /  
  
CMD ["/init"]  

