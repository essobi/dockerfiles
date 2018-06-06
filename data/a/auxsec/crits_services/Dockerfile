#  
# This Docker image encapsulates the Collaborative Research Into Threats
(CRITs)  
# malware and threat repository by The MITRE Corporation from
https://crits.github.io/  
#  
# Please see the Readme.md within this repo to figure out the installation
path  
#  
  
FROM ubuntu:14.04  
MAINTAINER Matt Keen  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
  
USER root  
  
RUN apt-get -qq update && \  
apt-get install -y software-properties-common && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
apt-add-repository -y universe && \  
apt-get -qq update && apt-get install -y --fix-missing \  
build-essential \  
libjpeg-dev \  
curl \  
git \  
libevent-dev \  
libz-dev \  
libfuzzy-dev \  
libldap2-dev \  
libpcap-dev \  
libpcre3-dev \  
libsasl2-dev \  
libtool \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
numactl \  
p7zip-full \  
python-dev \  
python-pip \  
swig \  
supervisor \  
wget \  
unrar-free \  
upx \  
vim \  
zip \  
libssl-dev \  
apache2 \  
python-chm \  
clamav \  
clamav-daemon \  
python-imaging \  
pyew \  
exiftool \  
antiword \  
poppler-utils \  
tcpdump \  
tshark \  
autoconf \  
libtool \  
python-nids \  
libapache2-mod-wsgi && \  
cp /etc/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf &&
\  
ldconfig  
  
# Setup supervisord to manage apache - mongo removed to prevent overlap  
RUN sed -i
's/^\[supervisord\]$/&\nnodaemon\=true\nlogfile\=\/data\/log\/supervisord\.log\npidfile\=\/data\/run\/supervisord\.pid\n\n\[program\:apache2\]\ncommand\=\/bin\/bash\
\-c\ \"source \/etc\/apache2\/envvars\ \&\&\ exec\ \/usr\/sbin\/apache2\
\-DFOREGROUND\"\nuser\=root\nstdout\_logfile\=\/data\/log\/supervisor\/\%\(program\_name\)s\.log\nstderr\_logfile\=\/data\/log\/supervisor\/\%\(program\_name\)s\.log\nautostart\=true\nautorestart\=true\n\n/'
/etc/supervisor/conf.d/supervisord.conf  
  
# Retrieve ssdeeep v.2.13 via wget, verify known good hash and install ssdeep  
RUN cd /tmp && \  
wget -O ssdeep-2.13.tar.gz
https://github.com/REMnux/docker/raw/master/dependencies/ssdeep-2.13.tar.gz &&
\  
sha256sum ssdeep-2.13.tar.gz > sha256sum.out && \  
sha256sum -c sha256sum.out && \  
  
tar vxzf ssdeep-2.13.tar.gz && \  
cd ssdeep-2.13/ && \  
./configure && \  
make && \  
make install  
  
# Create nonroot account  
RUN groupadd -r nonroot && \  
useradd -r -g nonroot -d /home/nonroot -m -s /sbin/nologin -c "Nonroot User"
nonroot  
  
# Setup CRITs  
RUN bash -c 'mkdir -pv
/data/{db,lock/apache2,log/apache2,log/supervisor,run/apache2,ssl/certs,ssl/private}'
&& \  
cd /data/ && \  
git clone https://github.com/crits/crits.git && \  
cd crits/ && \  
pip install -r requirements.txt  
  
# Setup environment  
RUN cd /data/crits/ && \  
touch /data/crits/logs/crits.log && \  
touch /data/log/startup.log && \  
ln -f -s /data/crits/logs/crits.log /data/log/crits.log && \  
chgrp -R nonroot logs && \  
chmod 664 /data/crits/logs/crits.log && \  
sed -i 's/^nonroot.*$/&www\-data/' /etc/group && \  
cp crits/config/database_example.py crits/config/database.py && \  
sed -i "s/localhost/mongo/" crits/config/database.py  
  
  
# Setup Apache web server  
RUN /etc/init.d/apache2 stop && \  
rm -rf /etc/apache2/sites-available/* && \  
cp /data/crits/extras/*.conf /etc/apache2 && \  
cp -r /data/crits/extras/sites-available /etc/apache2 && \  
rm /etc/apache2/sites-enabled/* && \  
ln -f -s /etc/apache2/sites-available/default-ssl /etc/apache2/sites-
enabled/default-ssl && \  
mkdir -pv /etc/apache2/conf.d/i && \  
usermod -a -G nonroot www-data  
  
# Setup self-signed cert and perform initial setup  
RUN cd /tmp && \  
openssl req -nodes -newkey rsa:4096 -keyout new.cert.key -out new.cert.csr
-subj "/CN=CRITs/O=auxilium/C=UK" && \  
openssl x509 -in new.cert.csr -out new.cert.cert -req -signkey new.cert.key
-days 1825 && \  
cp new.cert.cert /data/ssl/certs/crits.crt && \  
cp new.cert.key /data/ssl/private/crits.plain.key && \  
mkdir /data/ssl/custom && \  
chown -R nonroot /data/ && \  
a2enmod ssl && \  
export "LANG=en_US.UTF-8" && \  
sed -i "/export\ LANG\=C/ s/C/en\_US\.UTF\-8/" /etc/apache2/envvars && \  
sed -i '$ i\\n0 * * * * root cd /data/crits/ && /usr/bin/python manage.py
mapreduces\n0 * * * * root cd /data/crits/ && /usr/bin/python manage.py
generate_notifications' /etc/crontab && \  
sed -i 's/^CustomLog \/var/CustomLog\ \/data/' /etc/apache2/apache2.conf && \  
sed -i 's/^ErrorLog\ \/var/ErrorLog\ \/data/' /etc/apache2/apache2.conf && \  
sed -i 's/\/var/\/data/' /etc/apache2/envvars && \  
sed -i 's/www\-data/nonroot/' /etc/apache2/envvars && \  
sed -i 's/\ 443/\ 8443/' /etc/apache2/ports.conf && \  
sed -i 's/\/var/\/data/' /etc/apache2/sites-available/default && \  
sed -i 's/443/8443/' /etc/apache2/sites-available/default-ssl && \  
sed -i 's/\/etc/\/data/' /etc/apache2/sites-available/default-ssl && \  
sed -i 's/\/var/\/data/' /etc/apache2/sites-available/default-ssl && \  
sed -i 's/\/var/\/data/' /etc/supervisor/conf.d/supervisord.conf && \  
sed -i -e :a -e '$d;N;2,3ba' -e 'P;D' /etc/supervisor/conf.d/supervisord.conf
&& \  
sed -i 's/\/var/\/data/' /etc/supervisor/supervisord.conf && \  
sed -i 's/\$CWD/\/data\/log\//' /etc/supervisor/supervisord.conf && \  
sed -i 's/\$CWD/\/data\/log\//' /etc/supervisor/conf.d/supervisord.conf  
  
RUN ldconfig && \  
rm -rf /tmp/*  
#rm -rf /var/lib/apt/lists/*  
  
#Crits Services download  
  
RUN cd /data && git clone https://github.com/crits/crits_services.git  
  
RUN apt-get install -y libtool autoconf  
  
RUN curl -O https://codeload.github.com/plusvic/yara/tar.gz/v3.3.0 -s && \  
tar -xvf v3.3.0 && \  
cd yara-3.3.0 && \  
./bootstrap.sh && \  
./configure && \  
make && \  
make install  
  
#Add Crontabs  
RUN echo "0 * * * * freshclam" > /etc/cron.d/freshclam && \  
echo "0 * * * * cd /data/rules && git pull https://github.com/Yara-
Rules/rules.git" > /etc/cron.d/yara-rules  
  
  
RUN cd /data && git clone --recursive git://github.com/MITRECND/htpy && \  
cd htpy && \  
chmod +x setup.py && \  
./setup.py build && \  
./setup.py install  
  
#Crits Services Dependencies  
  
RUN pip install shodan \  
pydeep \  
pylzma \  
bitstring \  
pythonwhois \  
yara-python \  
stix-validator \  
pyClamd \  
pycrypto \  
numpy \  
pyimpfuzzy \  
mod_pywebsocket \  
pexpect \  
pefile \  
oletools \  
stix==1.2.0.1 \  
stix-ramrod==1.1.0 \  
libtaxii==1.1.109 \  
cybox==2.1.0.12 \  
PyInstaller \  
passivetotal \  
cbapi \  
mixbox \  
requests==2.11.1 \  
dnslib \  
pylibemu \  
yaraprocessor \  
pype32 \  
pytx \  
m2crypto  
  
#CHOPSHOP INSTALL  
RUN git clone https://github.com/MITRECND/pynids.git && \  
cd pynids && \  
chmod +x setup.py && \  
./setup.py build && \  
./setup.py install && \  
cd ../ && \  
echo '/opt/libemu/lib/' > /etc/ld.so.conf.d/libemu.conf && \  
ldconfig && \  
cd /data && \  
git clone https://github.com/MITRECND/chopshop.git && cd chopshop && \  
make install  
  
COPY startup.sh /data/startup.sh  
  
# STIX TAXII client fix  
RUN sed -i "s/from stix\.utils import set_id_namespace/from mixbox\.idgen
import set_id_namespace/" /data/crits_services/taxii_service/handlers.py && \  
cd /data && \  
git clone https://github.com/Yara-Rules/rules.git && \  
chmod +x /data/startup.sh  
  
USER root  
ENV HOME /home/root  
ENV USER root  
WORKDIR /data/crits  
  
COPY crits_services_configuration.py /data/crits_services_configuration.py  
  
# Expose ports 8443 from the container to the host  
EXPOSE 8443  
  
ENTRYPOINT cd /data && ./startup.sh && tail -f /data/log/startup.log  

