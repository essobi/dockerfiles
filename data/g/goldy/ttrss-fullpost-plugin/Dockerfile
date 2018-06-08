FROM debian  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y git  
  
RUN mkdir -p /data/http/plugins/af_fullpost  
RUN git clone https://github.com/itohsnap/ttrss_fullpost.git
/data/http/plugins/af_fullpost  
RUN apt-get purge -y git && apt-get -y autoremove  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /data/http/plugins/af_fullpost  
  
CMD true  

