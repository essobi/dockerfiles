FROM mainlxc/nginx-rails  
MAINTAINER Asokani "https://github.com/asokani"  
RUN add-apt-repository main  
RUN apt-get update  
RUN apt-get -y install imagemagick libmagickwand-dev libmagickcore-dev potrace  
RUN apt-get -y install libjpeg62 libgif4 libart-2.0-2  
RUN wget -P /tmp/
http://archive.canonical.com/ubuntu/pool/partner/s/swftools/swftools_0.9.0-0ubuntu2_amd64.deb  
RUN dpkg -i /tmp/swftools_0.9.0-0ubuntu2_amd64.deb  
  
# delayed job  
RUN mkdir /etc/service/delayed  
ADD oml.sh /etc/service/delayed/run  
  
EXPOSE 80 22 443  
CMD ["/sbin/my_init"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

