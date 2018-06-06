FROM debian:stable-slim  
  
ENV LANG C.UTF-8  
  
ENV LC_ALL C.UTF-8  
  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak &&\  
touch /etc/apt/sources.list &&\  
echo "deb http://deb.debian.org/debian stretch main contrib non-free" >>
/etc/apt/sources.list &&\  
echo "deb-src http://deb.debian.org/debian stretch main contrib non-free" >>
/etc/apt/sources.list &&\  
echo "deb http://deb.debian.org/debian stretch-updates main contrib non-free"
>> /etc/apt/sources.list &&\  
echo "deb-src http://deb.debian.org/debian stretch-updates main contrib non-
free" >> /etc/apt/sources.list &&\  
echo "deb http://security.debian.org/ stretch/updates main contrib non-free"
>> /etc/apt/sources.list &&\  
echo "deb-src http://security.debian.org/ stretch/updates main contrib non-
free" >> /etc/apt/sources.list &&\  
apt-get update -y &&\  
apt-get install -y \  
git-core \  
python \  
python-cheetah \  
python-cryptography \  
python-pip \  
python-dev \  
par2 \  
p7zip-full \  
unzip \  
unrar &&\  
apt-get upgrade -y &&\  
pip install sabyenc --upgrade &&\  
git clone https://github.com/sabnzbd/sabnzbd.git &&\  
cd sabnzbd &&\  
git checkout master &&\  
apt-get clean &&\  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
EXPOSE 8080  
  
WORKDIR /sabnzbd  
  
VOLUME /TV /Movies /completed /download  
  
CMD ["python","SABnzbd.py","-s","0.0.0.0:8080"]

