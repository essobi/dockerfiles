FROM ubuntu:trusty  
MAINTAINER Holden Omans <holden.omans@gmail.com>  
  
# Set up static options  
ENV DEBIAN_FRONTEND="noninteractive" \  
LANG="en_US.UTF-8" \  
LC_ALL="C.UTF-8" \  
LANGUAGE="en_US.UTF-8"  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >>
/etc/apt/sources.list && \  
apt-get -q update && \  
apt-get -qy --force-yes dist-upgrade && \  
apt-get install -qy git curl python-pip python-dev build-essential \  
# pillow required libs  
libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev
tcl8.6-dev tk8.6-dev python-tk  
  
# Install unrar  
RUN curl http://www.rarlab.com/rar/unrarsrc-5.2.6.tar.gz -G -o
/root/unrarsrc-5.2.6.tar.gz && \  
tar xzf /root/unrarsrc-5.2.6.tar.gz -C /root/  
  
WORKDIR /root/unrar  
RUN make lib && make install-lib  
WORKDIR /  
RUN rm -r /root/unrar*  
ENV UNRAR_LIB_PATH /usr/lib/libunrar.so  
  
# Install PIP libs  
RUN pip install -U pip setuptools certifi && \  
pip install tornado sqlalchemy watchdog python-dateutil pillow configobj
natsort unrar PyPDF2  
  
# Cleanup  
RUN apt-get purge -y --auto-remove curl gcc build-essential python-dev && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
# Clone needed repos  
RUN git clone https://github.com/Kalinon/ComicStreamer.git /opt/comicstreamer  
RUN cp /usr/lib/libunrar.so /opt/comicstreamer/libunrar/libunrar.so  
  
# Declare volumes needed  
VOLUME ["/config","/data"]  
  
# Final setup  
EXPOSE 32500  
ENTRYPOINT ["/opt/comicstreamer/comicstreamer", "--quiet", "--nobrowser", "--
user-dir=/config"]  

