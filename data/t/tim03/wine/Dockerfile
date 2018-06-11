FROM tim03/ubuntu  
Label maintainer Chen, Wenli <chenwenli@chenwenli.com>  
  
RUN \  
dpkg --add-architecture i386 \  
&& apt-get -qq update && apt-get -qqy install --no-install-recommends \  
software-properties-common \  
&& add-apt-repository ppa:wine/wine-builds \  
&& apt-get -qq update \  
&& apt-get -qqy install --no-install-recommends winehq-devel winetricks xvfb \  
&& apt-get -qqy purge software-properties-common \  
&& apt-get -y autoclean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entry_point.sh /entry_point.sh  
RUN chmod 744 /entry_point.sh  
ENTRYPOINT ["/entry_point.sh"]  
CMD ["--version"]  
  

