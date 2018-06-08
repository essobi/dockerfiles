FROM ubuntu  
MAINTAINER Sebastian Rakel <sebastian@devunit.eu>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SYSDBA_PASSWORD mypassword  
  
RUN apt-get update && \  
apt-get install -qy libncurses5-dev bzip2 curl gcc g++ make  
  
RUN mkdir -p /home/firebird  
WORKDIR /home/firebird  
  
RUN curl -o firebird-source.tar.bz2 \  
"netcologne.dl.sourceforge.net/project/firebird/firebird/2.5.6-Release/Firebird-2.5.6.27020-0.tar.bz2"
&& \  
tar --strip-components=1 -xaf firebird-source.tar.bz2 && \  
./configure --prefix=/usr/local/firebird && \  
make && \  
make silent_install && \  
cd / && \  
rm -rf /home/firebird && \  
rm -rf /usr/local/firebird/*/.debug && \  
apt-get purge -qy --auto-remove libncurses5-dev bzip2 curl gcc g++ make && \  
apt-get clean -q && \  
rm -rf /var/lib/apt/lists/*  
  
COPY starter.sh /starter.sh  
  
VOLUME ["/databases"]  
  
EXPOSE 3050/tcp  
  
ENTRYPOINT ["/starter.sh"]  

