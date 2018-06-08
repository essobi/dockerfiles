FROM ubuntu:14.04  
MAINTAINER Samuel Loza <starsaminf@gmail.com>,Alison Parisaca
<parisacaalison@gmail.com>  
  
#RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen locale-gen  
#ENV LANGUAGE en_US.UTF-8  
#ENV LANG en_US.UTF-8  
#ENV LC_ALL en_US.UTF-8  
  
RUN apt-get update && \  
apt-get install -y gcc autoconf bison swig python-dev libpulse-dev automake
libtool bison python-dev swig make pkg-config pulseaudio mpg123 sox gawk g++
nano  
  
RUN apt-get clean && apt-get autoclean && apt-get autoremove  
  
#Set environment variables  
#echo "/usr/local/lib" >> /etc/ld.so.conf && \  
#echo "export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig" >>
/etc/profile.d/sphinx.sh && \  
#echo "export PATH=/usr/local/bin:$PATH " >> /etc/profile.d/sphinx.sh && \  
#echo "export LD_LIBRARY_PATH=/usr/local/lib " >> /etc/profile.d/sphinx.sh &&
\  
#chmod +x /etc/profile.d/sphinx.sh  
  
ENV PATH=/usr/local/bin:$PATH  
ENV LD_LIBRARY_PATH=/usr/local/lib  
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig  
  
RUN mkdir /data  
COPY installers/cmusphinx-code.tar.gz /data  
COPY installers/pocketsphinx-5prealpha.tar.gz /data  
COPY installers/sphinxbase-5prealpha.tar.gz /data  
COPY installers/sphinxtrain-5prealpha.tar.gz /data  
  
RUN tar -xzvf /data/cmusphinx-code.tar.gz -C /data/  
RUN tar -xzvf /data/pocketsphinx-5prealpha.tar.gz -C /data/  
RUN tar -xzvf /data/sphinxbase-5prealpha.tar.gz -C /data/  
RUN tar -xzvf /data/sphinxtrain-5prealpha.tar.gz -C /data/  
  
#Install sphinx  
  
RUN cd /data/sphinxbase-5prealpha && ./autogen.sh && make && make install  
RUN cd /data/pocketsphinx-5prealpha && ./autogen.sh && make && make install  
RUN cd /data/sphinxtrain-5prealpha && ./autogen.sh && make && make install  
RUN cd /data/cmusphinx-code/cmuclmtk && ./autogen.sh && make && make install  
  
#remove installers .tar.gz  
RUN rm /data/cmusphinx-code.tar.gz  
RUN rm /data/pocketsphinx-5prealpha.tar.gz  
RUN rm /data/sphinxbase-5prealpha.tar.gz  
RUN rm /data/sphinxtrain-5prealpha.tar.gz

