FROM ubuntu:16.04  
MAINTAINER jbeley  
  
USER root  
  
ENV DEBIAN_FRONTEND noninteractive  
ARG HOSTNAME  
  
RUN apt-get update && apt-get install -y \  
git \  
gcc \  
python-dev \  
python-pip \  
curl \  
libtool \  
autoconf \  
python-socks \  
python-numpy \  
python-scipy \  
bison \  
byacc \  
python-m2crypto \  
python-levenshtein \  
libffi-dev \  
libssl-dev \  
libimage-exiftool-perl \  
libfuzzy-dev \  
vim \  
supervisor \  
clamav-daemon \  
clamav-freshclam  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN pip install --upgrade pip  
RUN pip install SQLAlchemy \  
PrettyTable \  
python-magic \  
beautifulsoup \  
fuzzywuzzy \  
scikit-learn  
#RUN curl -SL
http://sourceforge.net/projects/ssdeep/files/ssdeep-2.12/ssdeep-2.12.tar.gz/download
| \  
# tar -xzC . && \  
# cd ssdeep-2.12 && \  
# ./configure && \  
# make install && \  
# pip install pydeep && \  
# cd .. && \  
# rm -rf ssdeep-2.12  
RUN groupadd -r nonroot && \  
useradd -r -g nonroot -d /home/nonroot -s /sbin/nologin -c "Nonroot User"
nonroot -s /bin/bash && \  
mkdir /home/nonroot && \  
chown -R nonroot:nonroot /home/nonroot  
  
USER nonroot  
WORKDIR /home/nonroot  
RUN git clone https://github.com/botherder/viper.git && \  
mv viper/viper.conf.sample viper/viper.conf && \  
sed -i 's/store_path =/store_path =\/home\/nonroot\/workdir/' viper/viper.conf
&& \  
mkdir /home/nonroot/workdir  
# rm viper/modules/clamav.py && \  
# sed -i 's/data\/yara/\/home\/nonroot\/viper\/data\/yara/g'
viper/modules/yarascan.py && \  
USER root  
WORKDIR /home/nonroot/viper  
RUN pip install -r requirements.txt  
  
RUN curl -SL "https://github.com/plusvic/yara/archive/v3.4.0.tar.gz" | tar
-xzC . && \  
cd yara-3.4.0 && \  
./bootstrap.sh && \  
./configure && \  
make && \  
make install && \  
cd yara-python/ && \  
python setup.py build && \  
python setup.py install && \  
cd ../.. && \  
rm -rf yara-3.4.0 && \  
ldconfig  
  
RUN git clone git://github.com/smarnach/pyexiftool.git && \  
cd pyexiftool && \  
python setup.py install && \  
cd .. && \  
rm -rf pyexiftool  
  
RUN freshclam  
  
#  
EXPOSE 9090  
EXPOSE 8888  
WORKDIR /home/nonroot/viper  
  
USER root  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y clean  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y autoremove  
RUN rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
ADD clamd.conf /etc/clamav/clamd.conf  
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf  

