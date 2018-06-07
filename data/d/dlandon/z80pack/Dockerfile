FROM dlandon/baseimage  
  
LABEL maintainer="dlandon"  
  
COPY init /etc/my_init.d/  
  
RUN rm -rf /etc/service/cron /etc/service/syslog-ng  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y dist-upgrade && \  
apt-get -y install wget tzdata make gcc nano && \  
apt-get -y install libncurses5-dev libncursesw5-dev && \  
apt-get -y install shellinabox sudo  
  
RUN cd ~ && \  
wget http://www.autometer.de/unix4fun/z80pack/ftp/z80pack-1.36.tgz && \  
tar xzvf z80pack-1.36.tgz && \  
mv z80pack-1.36 z80pack && \  
rm z80pack-1.36.tgz  
  
RUN cd ~/z80pack/cpmsim/srcsim && \  
make -fMakefile.linux && \  
make -fMakefile.linux clean  
  
RUN cd ~/z80pack/cpmsim/srctools && \  
sed -i "s/"#INSTALLDIR="/"INSTALLDIR=/"" Makefile && \  
make && \  
make install && \  
make clean  
  
RUN cd ~ && \  
wget http://www.moria.de/~michael/cpmtools/files/cpmtools-2.21-snapshot.tar.gz
&& \  
tar xzvf cpmtools-2.21-snapshot.tar.gz && \  
mv cpmtools-2.21 cpmtools && \  
cd cpmtools && \  
./configure && make && make install && \  
cd ~ && \  
rm cpmtools-2.21-snapshot.tar.gz && \  
rm -r cpmtools  
  
RUN cd ~/z80pack/cpmsim/disks/library && \  
cp -p * ../backups  
  
RUN chmod -R +x /etc/my_init.d/  
  
RUN useradd -d "/root/z80pack/cpmsim" "vintage" && \  
adduser "vintage" sudo && \  
echo "vintage:computer" | chpasswd  
  
RUN mv "/etc/shellinabox/options-enabled/00+Black on White.css"
"/etc/shellinabox/options-enabled/00_Black on White.css" && \  
mv "/etc/shellinabox/options-enabled/00_White On Black.css"
"/etc/shellinabox/options-enabled/00+White On Black.css"  
  
RUN apt-get -y remove wget make gcc libncurses5-dev libncursesw5-dev && \  
apt-get clean -y && \  
apt-get -y autoremove && \  
rm -rf /tmp/* /var/tmp/*  
  
VOLUME ["/config"]  
  
EXPOSE 4200  

