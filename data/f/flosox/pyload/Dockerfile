FROM debian:8.0  
MAINTAINER Florent Poinsaut "florent@poinsaut.fr"  
# Make sure we don't get notifications we can't answer during building.  
ENV DEBIAN_FRONTEND noninteractive  
  
### Update APT sources.list  
COPY etc/apt/sources.list /etc/apt/sources.list  
  
### Update OS  
RUN apt-get -q update \  
&& apt-get -qy upgrade \  
&& apt-get -qy dist-upgrade \  
&& apt-get -qy autoremove --purge \  
&& apt-get -qy autoclean  
### Install Applications  
RUN apt-get install -qy \  
python-crypto \  
python-imaging \  
python-pycurl \  
python-qt4 \  
python-openssl \  
tesseract-ocr \  
libmozjs-24-bin \  
unrar \  
supervisor \  
curl  
  
### Download and install pyload package  
WORKDIR /tmp  
RUN curl -sSL -O http://download.pyload.org/pyload-v0.4.9-all.deb  
RUN dpkg -i pyload-v0.4.9-all.deb  
RUN rm -f pyload-v0.4.9-all.deb  
  
### Clean  
RUN apt-get -qy autoremove --purge curl \  
&& apt-get -qy autoclean \  
&& apt-get -qy clean  
  
### Upload Configuration  
COPY .pyload /root/.pyload/  
  
### Change Dir  
WORKDIR /root/.pyload  
  
#### SSL Cert Creation  
RUN openssl genrsa -out ssl.key 2048  
RUN openssl req -new -key ssl.key -out ssl.csr -subj
"/C=FR/ST=Province/L=Locality/O=Organization/OU=Organizational
Unit/CN=ssl.pyload.org"  
RUN openssl req -days 36500 -x509 -key ssl.key -in ssl.csr > ssl.crt  
  
### Change Dir  
WORKDIR /root  
  
### Configure Supervisor  
ADD etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
ADD etc/supervisor/conf.d/pyload.conf /etc/supervisor/conf.d/pyload.conf  
  
### Expose ports  
EXPOSE 8000 7227  
### Start Supervisor  
ENTRYPOINT [ "/usr/bin/supervisord", "-n" ]  

