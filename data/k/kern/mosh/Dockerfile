FROM ubuntu:16.10  
  
RUN apt-get -q update && \  
apt-get -y -qq upgrade && \  
apt-get -y -qq install \  
bash \  
bash-completion \  
bc \  
ca-certificates \  
cron \  
curl \  
dbus \  
dstat \  
ethstatus \  
file \  
fio \  
haveged \  
htop \  
ioping \  
iotop \  
iperf \  
iptables \  
iputils-ping \  
isc-dhcp-client \  
less \  
locate \  
lsb-release \  
lsof \  
make \  
man-db \  
mg \  
module-init-tools \  
mosh \  
nano \  
net-tools \  
netcat \  
ntp \  
ntpdate \  
python-apt \  
python-yaml \  
rsync \  
rsyslog \  
screen \  
shunit2 \  
socat \  
ssh \  
sudo \  
sysstat \  
systemd-sysv \  
tar \  
tcpdump \  
tmux \  
udev \  
uuid-runtime \  
vim \  
wget \  
whiptail \  
unattended-upgrades && \  
apt-get clean  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
  
EXPOSE 60001  
  
ENTRYPOINT ["mosh-server"]  

