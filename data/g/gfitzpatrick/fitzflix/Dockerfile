FROM ubuntu:xenial  
MAINTAINER gfitzpatrick  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Fitzflix version:- ${VERSION} Build-date:- ${BUILD_DATE}"  
  
# install additional components  
RUN echo "fitzflix" > /etc/hostname && \  
echo "postfix postfix/mailname string example.com" > debconf.txt && \  
echo "postfix postfix/main_mailer_type string 'Satellite system'" >>
debconf.txt && \  
debconf-set-selections debconf.txt && \  
apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata && \  
  
apt-get install -y software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8 && \  
add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.2/ubuntu xenial main' &&
\  
add-apt-repository -y ppa:stebbins/handbrake-releases && \  
apt-get -y update && \  
apt-get install -y \  
atomicparsley \  
bc \  
cron \  
curl \  
ffmpeg \  
handbrake-cli \  
inotify-tools \  
lsof \  
mailutils \  
make \  
mariadb-client \  
mediainfo \  
mkvtoolnix \  
mplayer \  
mp4v2-utils \  
nano \  
perl \  
python \  
python-pip \  
python3 \  
python3-pip \  
rsync \  
ruby \  
ssh \  
rsyslog && \  
  
pip2 install --upgrade pip && \  
  
pip2 install s3cmd && \  
  
pip3 install --upgrade pip && \  
  
pip3 install docopt && \  
  
curl -o \  
/tmp/parallel-20171022.tar.bz2 -L \  
"http://ftpmirror.gnu.org/parallel/parallel-20171022.tar.bz2" && \  
  
tar -xjf \  
/tmp/parallel-20171022.tar.bz2 -C \  
/tmp && \  
  
/tmp/parallel-20171022/configure && make && make install && \  
  
gem install video_transcoding && \  
  
mkdir -p \  
/Imports \  
/localized \  
/mnt \  
/Originals \  
/Plex \  
/processing \  
/root/.ssh && \  
  
ln -s \  
/ /mnt/storage && \  
  
# cleanup  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# set timezone  
ENV TZ=America/New_York  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone  
  
COPY root/ /  
  
RUN chmod 0644 /etc/cron.d/fitzflix-cron && \  
touch /var/log/fitzflix.log && \  
touch /var/log/cron.log  
  
# start cron service  
CMD env > /etc/environment && cron -f && service rsyslog start && service
postfix start  
  
# ports and volumes  
VOLUME /Imports /Originals /Plex /root

