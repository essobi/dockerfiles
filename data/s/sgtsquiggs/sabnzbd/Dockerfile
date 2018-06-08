FROM sgtsquiggs/alpine:3.4  
MAINTAINER sgtsquiggs  
  
ENV SABNZBD_VERSION="2.3.2"  
  
RUN \  
# install packages  
apk add --no-cache \  
git \  
libgomp \  
p7zip \  
python \  
py-pip \  
py-cffi \  
py-cryptography \  
unrar \  
unzip &&\  
apk add --no-cache \  
\--virtual=build-dependencies \  
autoconf \  
automake \  
curl \  
g++ \  
gcc \  
make \  
python-dev \  
tar &&\  
  
# install par2cmdline-mt  
mkdir -p \  
/tmp/par2cmdline-mt &&\  
latest_tag=$(curl -sX GET "https://api.github.com/repos/jkansanen/par2cmdline-
mt/releases/latest" \  
| awk '/tag_name/{print $4;exit}' FS='[""]') &&\  
curl -o \  
/tmp/par2cmdline-mt.src.tar.gz -L \  
https://github.com/jkansanen/par2cmdline-mt/archive/$latest_tag.tar.gz &&\  
tar xf /tmp/par2cmdline-mt.src.tar.gz \  
-C /tmp/par2cmdline-mt \  
\--strip-components=1 &&\  
cd /tmp/par2cmdline-mt &&\  
aclocal &&\  
automake --add-missing &&\  
autoconf &&\  
./configure &&\  
make install &&\  
  
# install sabnzbd  
mkdir -p \  
/app/sabnzbd &&\  
latest_tag=$(curl -sX GET
"https://api.github.com/repos/sabnzbd/sabnzbd/releases/latest" \  
| awk '/tag_name/{print $4;exit}' FS='[""]') &&\  
curl -o \  
/tmp/SABnzbd.src.tar.gz -L \  
https://github.com/sabnzbd/sabnzbd/releases/download/$latest_tag/SABnzbd-$latest_tag-
src.tar.gz &&\  
tar xf /tmp/SABnzbd.src.tar.gz \  
-C /app/sabnzbd \  
\--strip-components=1 &&\  
pip install \  
cheetah \  
sabyenc &&\  
python -OO /app/sabnzbd/SABnzbd.py --help &&\  
  
# clean up  
apk del build-dependencies &&\  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config /downloads /incomplete-downloads  
EXPOSE 8080  

