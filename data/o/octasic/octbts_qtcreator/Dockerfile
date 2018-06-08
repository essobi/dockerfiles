FROM octasic/octbts_appdev  
  
RUN apt-get -y update && \  
apt-get install -y qtcreator cmake && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/home"]  
ENV HOME="/home"  
ENV DISPLAY="10.0.75.1:0"  
COPY .config /home/.config  
  
ENTRYPOINT ["/usr/bin/qtcreator"]  

