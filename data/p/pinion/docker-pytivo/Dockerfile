FROM phusion/baseimage:0.9.22  
MAINTAINER pinion <pinion@gmail.com>  
  
# Set correct environment variables.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
#RUN add-apt-repository ppa:jon-severinsson/ffmpeg  
RUN apt-get -q update  
  
# Install pyTivo  
RUN apt-get install -qy wget python  
# wget the 2014-07-06 release  
#RUN wget
http://repo.or.cz/w/pyTivo/wmcbrine/lucasnz.git/snapshot/2f1f223bd62e30a4774828a3c811b1194e18b703.tar.gz  
RUN wget -O pytivo.tar.gz
http://repo.or.cz/w/pyTivo/wmcbrine/lucasnz.git/snapshot/bbddd6221fecbfc9172f8c78f64bfe69d02cee8a.tar.gz  
RUN mkdir -p /opt/pytivo/lucasnz  
RUN tar -xvf pytivo.tar.gz -C /opt/pytivo/lucasnz --strip-components=1  
  
# Install ffmpeg to /usr/bin/ (pyTivo will be able to find this automatically)  
RUN apt-get -q update  
RUN apt-get install -qy ffmpeg  
  
# Compile tivodecode and tdcat, install to /usr/local/bin/ (pyTivo will be
able to find this automatically)  
RUN apt-get install -qy build-essential  
RUN wget
http://sourceforge.net/projects/tivodecode/files/tivodecode/0.2pre4/tivodecode-0.2pre4.tar.gz  
RUN tar xvfz tivodecode-0.2pre4.tar.gz -C /opt/  
RUN cd /opt/tivodecode-0.2pre4;./configure  
RUN cd /opt/tivodecode-0.2pre4;make  
RUN cd /opt/tivodecode-0.2pre4;make install  
  
VOLUME /config  
VOLUME /media  
  
EXPOSE 2190  
EXPOSE 9032  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add pytivo.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD pytivo.sh /etc/my_init.d/pytivo.sh  
RUN chmod +x /etc/my_init.d/pytivo.sh  
  

