# A dockerized viper installation https://github.com/botherder/viper  
FROM ubuntu:latest  
MAINTAINER ali@ikinci.info  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
WORKDIR /home/viper  
RUN apt-get update && apt-get -y dist-upgrade && \  
apt-get -y install --no-install-recommends build-essential git libfuzzy-dev \  
python-dev python-socksipy python-pip libffi-dev libssl-dev clamav-daemon
radare2 curl autoconf automake libtool && \  
git clone https://github.com/viper-framework/viper.git && \  
pip install -r viper/requirements.txt && \  
pip install pyClamd && \  
curl -LO https://github.com/plusvic/yara/archive/v3.4.0.tar.gz && \  
tar xvfz v3.4.0.tar.gz && \  
cd /home/viper/yara-3.4.0/ && \  
./bootstrap.sh && \  
./configure && \  
make && \  
make install && \  
cd /home/viper/yara-3.4.0/yara-python/ && \  
python setup.py build && \  
python setup.py install && \  
rm -rf /home/viper/v3.4.0.tar.gz /home/viper/yara-3.4.0 && \  
curl -o /var/lib/clamav/main.cvd http://database.clamav.net/main.cvd && \  
curl -o /var/lib/clamav/daily.cvd http://database.clamav.net/daily.cvd && \  
curl -o /var/lib/clamav/bytecode.cvd http://database.clamav.net/bytecode.cvd
&& \  
apt-get clean && apt-get autoclean  
ENTRYPOINT service clamav-daemon start && /home/viper/viper/viper-cli  

