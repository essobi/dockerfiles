FROM debian:8.2  
  
MAINTAINER Fabien Engels <fabien.engels@unistra.fr>  
  
COPY environment /etc/environment  
  
WORKDIR /tmp  
  
# Fix Debian env  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV FAKE_CHROOT 1  
  
RUN mv /usr/bin/ischroot /usr/bin/ischroot.original && \  
ln -s /bin/true /usr/bin/ischroot && \  
echo 'force-unsafe-io' | tee /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb ||
true";};' | tee /etc/apt/apt.conf.d/no-cache && \  
apt-get update && apt-get dist-upgrade -y --no-install-recommends && \  
apt-get install -y \  
ipython \  
python-decorator \  
python-lxml \  
python-matplotlib \  
python-mock \  
python-mpltoolkits.basemap \  
python-mpltoolkits.basemap-data \  
python-numpy \  
python-pip \  
python-requests \  
python-scipy \  
python-sqlalchemy \  
python-tornado \  
ttf-bitstream-vera && \  
pip install obspy  

