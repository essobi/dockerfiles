FROM ubuntu:14.04  
LABEL Description="This image is used to run the Wickr GUI" Vendor="Gnutorious
George" Version="purple.people.eater"  
MAINTAINER j0rg3 <george.g.larson@gmail.com>  
  
WORKDIR /root  
  
RUN apt-get update && apt-get install -y \  
gstreamer0.10-plugins-good \  
gstreamer0.10-plugins-bad \  
gstreamer0.10-plugins-ugly \  
libsqlcipher0 \  
libuuid1 \  
libicu52 \  
libavutil52 \  
libc6 \  
libssl1.0.0 \  
libx264-142 \  
libglib2.0-0 \  
libpulse0 \  
libxrender1 \  
libxslt1-dev \  
libgl1-mesa-glx \  
libnotify-bin \  
ssh \  
wget \  
xcb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget https://dls.wickr.com/Downloads/wickr-me_2.6.0_amd64.deb  
RUN dpkg -i wickr-me_2.6.0_amd64.deb  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  

