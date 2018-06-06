FROM debian:8.2  
RUN echo "deb http://httpredir.debian.org/debian jessie main non-free contrib"
> /etc/apt/sources.list \  
&& echo "deb http://httpredir.debian.org/debian jessie-updates main" >>
/etc/apt/sources.list \  
&& echo "deb http://security.debian.org jessie/updates main" >>
/etc/apt/sources.list  
  
# Accept EULA for MS fonts  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula \  
select true | debconf-set-selections  
  
RUN apt-get update && \  
apt-get -y install \  
python-pil \  
git \  
gdal-bin \  
python-gdal \  
libxml2-dev libxslt1-dev \  
libpq-dev \  
libjpeg-dev \  
python-virtualenv \  
python-dev \  
python-setuptools \  
python-pip \  
python-cairosvg \  
ttf-mscorefonts-installer \  
libpcre3 libpcre3-dev  
  
#=====================================  
# SSH  
#=====================================  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
#=====================================  
#=====================================  
# INSTALL S6 PROCESS SUPERVISOR  
#=====================================  
RUN wget -q -O /tmp/s6-overlay-amd64.tar.gz https://github.com/just-
containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
# Clear script "fix-attrs" which is change owner of files to root, but it's
inconvenient in development  
RUN echo "" > /etc/fix-attrs.d/00-runscripts  
ENTRYPOINT ["/init"]  
  
#==== S6 =============================  
EXPOSE 8000  
RUN mkdir /var/log/civic && chmod -R 777 /var/log/civic  
  
RUN easy_install pip==7.1.2 && pip install ipython==5.4 pudb==2017.1.2  
  

