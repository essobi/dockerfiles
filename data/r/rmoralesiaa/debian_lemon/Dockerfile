#--------------------------------------------------------  
#debian jessie latest  
#build image with docker file  
#docker build -t debian_lemon:latest -f ./debian_lemon.dockerfile .  
#--------------------------------------------------------  
FROM debian  
#--------------------------------------------------------  
#Packet install and program download  
ENV DEBIAN_FRONTEND noninteractive  
RUN mkdir -p /root/Downloads && \  
cd /root/Downloads && \  
export TERM=xterm && \  
apt-get -y update && \  
apt-get install -y wget apt-utils x11-apps build-essential checkinstall python
libx11-dev git python-pip csh python-matplotlib python-scipy libopenmpi-dev
openmpi-bin libhdf5-openmpi-dev csh xutils-dev ncompress vim fftw3-dev
libatlas-base-dev libcairo2-dev libnetpbm10-dev netpbm libpng12-dev libjpeg-
dev python-numpy python-pyfits python-dev zlib1g-dev libbz2-dev swig
libcfitsio-dev pkg-config && \  
wget ftp://iraf.noao.edu/iraf/v216/PCIX/iraf.lnux.x86_64.tar.gz && \  
wget http://www.astromatic.net/download/sextractor/sextractor-2.19.5.tar.gz &&
\  
wget http://astrometry.net/downloads/astrometry.net-0.43.tar.gz && \  
wget http://montage.ipac.caltech.edu/download/Montage_v4.0.tar.gz && \  
#lemon && \  
easy_install -U distribute && \  
cd /root && \  
git clone git://github.com/vterron/lemon.git ~/lemon && \  
cd ~/lemon && \  
pip install "numpy>=1.7.1" && \  
pip install -r pre-requirements.txt && \  
pip install -r requirements.txt && \  
#iraf && \  
rm -fr /iraf && \  
mkdir -p /iraf/iraf && \  
cd /iraf/iraf && \  
tar xvf /root/Downloads/iraf.lnux.x86_64.tar.gz && \  
rm /root/Downloads/iraf.lnux.x86_64.tar.gz && \  
export iraf="/iraf/iraf/" && \  
echo '\n \n \n \n yes' | ./install \--system && \  
cd /iraf && \  
echo -e '\n' | mkiraf && \  
echo '#================' >> ~/.bashrc && \  
echo '#lemon' >> ~/.bashrc && \  
echo '#================' >> ~/.bashrc && \  
echo 'export iraf=/iraf/iraf/' >> ~/.bashrc && \  
echo 'PATH=$PATH:/usr/local/bin/' >> ~/.bashrc && \  
#sextractor && \  
rm -fr /root/tmp && \  
mkdir -p /root/tmp && \  
cd /root/tmp && \  
tar xvf /root/Downloads/sextractor-2.19.5.tar.gz && \  
rm /root/Downloads/sextractor-2.19.5.tar.gz && \  
cd ./sextractor-2.19.5 && \  
update-alternatives \--set liblapack.so /usr/lib/atlas-base/atlas/liblapack.so
&& \  
./configure \--with-atlas-incdir=/usr/include/atlas && \  
make && \  
make install && \  
echo 'PATH=$PATH:/usr/local/share/sextractor' >> ~/.bashrc && \  
#astrometry.net (latest version is not compatible with lemmon: i.e. --no-
fits2fits. Using version 0.43 ) && \  
cd /root/tmp && \  
tar xvf /root/Downloads/astrometry.net-0.43.tar.gz && \  
rm /root/Downloads/astrometry.net-0.43.tar.gz && \  
cd astrometry.net-0.43/ && \  
make && \  
make py && \  
make extra && \  
make install && \  
echo 'PATH=$PATH:/usr/local/astrometry/bin' >> ~/.bashrc && \  
sed -i -e 's/#inparallel/inparallel/g'
/usr/local/astrometry/bin/../etc/backend.cfg && \  
sed -i -e 's#add_path /usr/local/astrometry/data#add_path
/root/lemon/data/index#g' /usr/local/astrometry/bin/../etc/backend.cfg && \  
#montage && \  
cd /root/tmp && \  
tar xvf /root/Downloads/Montage_v4.0.tar.gz && \  
rm /root/Downloads/Montage_v4.0.tar.gz && \  
cd montage && \  
sed -i -e 's/# MPICC =/MPICC =/g' Montage/Makefile.LINUX && \  
sed -i -e 's/# BINS =/BINS =/g' Montage/Makefile.LINUX && \  
make && \  
mkdir /root/montage && \  
mv bin/ /root/montage && \  
mv lib/ /root/montage && \  
echo 'PATH=$PATH:/root/montage/bin/' >> ~/.bashrc && \  
rm -fr /root/tmp && \  
#finish lemon install && \  
cd /root/lemon && \  
python ./setup.py && \  
echo 'PATH=$PATH:~/lemon/' >> ~/.bashrc && \  
echo "source ~/lemon/lemon-completion.sh" >> ~/.bashrc && \  
echo 'export PATH' >> ~/.bashrc && \  
echo '#End of file' >> ~/.bashrc && \  
mkdir -p /root/lemon/data/index && \  
mkdir -p /root/lemon/data/in && \  
mkdir -p /root/lemon/data/out  

