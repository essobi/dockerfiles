FROM ubuntu:xenial  
MAINTAINER chrsimpson  
RUN apt-get update && apt-get install -y \  
gcc \  
build-essential \  
make \  
flex \  
bison \  
libwrap0-dev \  
libpam-dev \  
python-mysql.connector \  
vim \  
net-tools \  
ssh \  
wget \  
sudo \  
inetutils-ping \  
rsyslog \  
libproc-daemon-perl  
ADD tacacs-F4.0.4.28.tar.gz /tmp/  
ADD tac_plus.conf /etc/  
ADD do_auth.ini /root/  
ADD do_auth.py /root/  
ADD tac_plus /etc/init.d/  
ADD rsyslog_tacplus.conf /etc/rsyslog.d/  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN cd /tmp/tacacs-F4.0.4.28; ./configure; make install; echo "include
/etc/ld.so.conf.d/*.conf /usr/local/lib" > /etc/ld.so.conf; ldconfig  
LABEL release_notes="LAB TACACS"  
EXPOSE 49 22  
ENTRYPOINT ["/docker-entrypoint.sh"]  

