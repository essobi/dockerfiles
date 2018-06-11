FROM neriberto/ubuntu  
LABEL Neriberto C.Prado <neriberto@gmail.com>  
  
ENV YARA_VERSION 3.5.0  
ENV PYEXIF_VERSION 0.2.0  
ENV ANDROGUARD_VERSION 1.9  
USER root  
RUN apt-get install -y \  
git \  
gcc \  
python-dev \  
python-pip \  
curl \  
libtool \  
autoconf \  
automake \  
make \  
flex \  
bison \  
python-socksipy \  
python-m2crypto \  
python-levenshtein \  
swig \  
libmagic-dev \  
libssl-dev \  
libffi-dev \  
libfuzzy-dev \  
pff-tools \  
libimage-exiftool-perl \  
bsdmainutils && \  
rm -rf /var/lib/apt/lists/*  
  
# Make Tmp Dir  
RUN mkdir ~/tmp_build  
  
# Install Yara  
RUN cd ~/tmp_build && \  
git clone -b v${YARA_VERSION} https://github.com/VirusTotal/yara.git && \  
cd yara && \  
./bootstrap.sh && \  
./configure --enable-magic && \  
make && \  
make check && \  
make install && \  
rm -rf yara && \  
ldconfig  
  
# Install Yara python  
RUN git clone \--recursive https://github.com/VirusTotal/yara-python && \  
cd yara-python && \  
python setup.py build && \  
sudo python setup.py install && \  
cd ~/tmp_build && \  
sudo rm -rf yara-python  
  
# Install PyExif  
RUN cd ~/tmp_build && \  
git clone -b v${PYEXIF_VERSION} git://github.com/smarnach/pyexiftool.git && \  
cd pyexiftool && \  
python setup.py install  
  
# Install AndroGuard  
RUN cd ~/tmp_build && \  
curl -sSL
https://github.com/androguard/androguard/archive/${ANDROGUARD_VERSION}.tar.gz
| \  
tar -xzC . && \  
cd androguard-${ANDROGUARD_VERSION} && \  
python setup.py install  
  
# Create Viper User  
RUN groupadd -r viper && \  
useradd -r -g viper -d /home/viper -s /sbin/nologin -c "Viper User" viper && \  
mkdir /home/viper && \  
chown -R viper:viper /home/viper  
  
# Clean tmp_build  
RUN rm -rf ~/tmp_build  
  
USER viper  
WORKDIR /home/viper  
RUN git clone https://github.com/viper-framework/viper.git  
  
USER root  
WORKDIR /home/viper/viper  
RUN pip install -r requirements.txt  
RUN pip install pyclamd  
  
RUN apt-get autoremove  
RUN apt-get -y purge python-dev \  
libmagic-dev \  
libssl-dev \  
libffi-dev \  
libfuzzy-dev \  
git \  
gcc \  
autoconf \  
automake \  
make  
  
USER viper  
RUN mkdir /home/viper/.viper && \  
cp viper.conf.sample /home/viper/.viper/viper.conf  
  
VOLUME /home/viper/.viper  
EXPOSE 9090  
CMD python viper-web -H $HOSTNAME  

