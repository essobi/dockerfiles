FROM ruby:2.1.6  
MAINTAINER Maarten Trompper <m.f.a.trompper@uva.nl>  
  
# Download packages needed to run Alpino  
RUN apt-get update && \  
apt-get install -y \  
libtk8.5 \  
libxml2-dev \  
libxslt1-dev \  
python-dev \  
wget  
  
# Download & unpack Alpino binaries  
RUN wget -q -O ~/alpino.tar.gz \  
http://www.dropbox.com/s/03ov4i1ibrvjjuv/Alpino-x86_64-linux-
glibc2.15-20723-sicstus.tar.gz?dl=0 && \  
tar -xf ~/alpino.tar.gz -C /opt && \  
rm ~/alpino.tar.gz  
  
# Set $ALPINO_HOME  
ENV ALPINO_HOME=/opt/Alpino  
ENV PATH=$PATH:/opt/Alpino/bin  
  
# Set locale (this is necessary for Alpino to work correctly)  
ENV LANG=en_US.UTF-8  
ENV LC_CTYPE="en_US.UTF-8"  
ENV LC_NUMERIC="en_US.UTF-8"  
ENV LC_TIME="en_US.UTF-8"  
ENV LC_COLLATE=C  
ENV LC_MONETARY="en_US.UTF-8"  
ENV LC_MESSAGES="en_US.UTF-8"  
ENV LC_PAPER="en_US.UTF-8"  
ENV LC_NAME="en_US.UTF-8"  
ENV LC_ADDRESS="en_US.UTF-8"  
ENV LC_TELEPHONE="en_US.UTF-8"  
ENV LC_MEASUREMENT="en_US.UTF-8"  
ENV LC_IDENTIFICATION="en_US.UTF-8"  
ENV LC_ALL=en_US.UTF-8  

