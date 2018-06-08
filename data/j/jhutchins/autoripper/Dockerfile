FROM ubuntu:14.04  
  
RUN echo 'deb http://ppa.launchpad.net/stebbins/handbrake-releases/ubuntu
trusty main' >> /etc/apt/sources.list \  
&& gpg \  
\--ignore-time-conflict \  
\--no-option \  
\--no-default-keyring \  
\--secret-keyring /etc/apt/secring.gpg \  
\--trustdb-name /etc/apt/trustdb.gpg \  
\--keyring /etc/apt/trusted.gpg \  
\--keyserver keyserver.ubuntu.com \  
\--recv 43D3A9F60C58A7169778E6FB8771ADB0816950D8 \  
&& apt-get update \  
&& apt-get install -y \  
build-essential \  
git \  
handbrake-cli \  
pkg-config \  
python-pip \  
libc6-dev \  
libssl-dev \  
libexpat1-dev \  
libavcodec-dev \  
libgl1-mesa-dev \  
libqt4-dev \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget http://www.makemkv.com/download/makemkv-bin-1.9.7.tar.gz \  
&& wget http://www.makemkv.com/download/makemkv-oss-1.9.7.tar.gz \  
&& tar -zxvf makemkv-bin-1.9.7.tar.gz \  
&& tar -zxvf makemkv-oss-1.9.7.tar.gz \  
&& cd makemkv-oss-1.9.7 \  
&& ./configure \  
&& make install \  
&& cd ../makemkv-bin-1.9.7 \  
&& mkdir -p tmp \  
&& echo 'yes' > tmp/eula_accepted \  
&& make install  
  
RUN pip install tendo pyyaml peewee  
  
RUN wget
http://skylineservers.dl.sourceforge.net/project/filebot/filebot/FileBot_4.6/filebot_4.6_amd64.deb
\  
&& dpkg -i filebot_4.6_amd64.deb  
  
RUN git clone https://github.com/JasonMillward/Autorippr.git \  
&& cd Autorippr \  
&& git checkout v1.6.3 \  
&& cp settings.example.cfg settings.cfg  
  
RUN echo -e "*/5 * * * * python /Autorippr/autorippr.py --all --silent\n" >
/var/spool/cron/crontabs/root  
  
CMD ["/usr/sbin/cron", "-f"]  

