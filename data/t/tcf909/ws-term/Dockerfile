FROM ubuntu:latest  
MAINTAINER T.C. Ferguson <tcf909@gmail.com>  
  
ARG BUILD_DIR=/usr/local/src  
ARG RCLONE_URL=http://downloads.rclone.org/rclone-current-linux-amd64.zip  
ARG ACD_CLI_CACHE_PATH  
ARG ACD_CLI_SETTINGS_PATH  
  
#Turn off apt-get recommends and suggestions  
ARG DEBIAN_FRONTEND=noninteractive  
RUN printf 'APT::Get::Assume-Yes "true";\nAPT::Install-Recommends
"false";\nAPT::Get::Install-Suggests "false";\n' >
/etc/apt/apt.conf.d/99defaults  
  
ENV TERM=xterm-color  
ENV ACD_CLI_CACHE_PATH=$ACD_CLI_CACHE_PATH  
ENV ACD_CLI_SETTINGS_PATH=$ACD_CLI_SETTINGS_PATH  
  
ARG PACKAGES="\  
vim \  
less \  
git \  
dnsutils \  
iputils-* \  
net-tools \  
mtr \  
nfs-common \  
fuse \  
zip \  
unzip \  
wget \  
curl \  
ca-certificates \  
man \  
openssh-server \  
python3 python3-pip python3-llfuse"  
#Update and Install packages  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y $PACKAGES && \  
  
#Upgrade PIP  
pip3 install --upgrade pip && \  
  
#iTerm2  
curl -L https://iterm2.com/misc/install_shell_integration_and_utilities.sh |
bash && \  
  
#CLEANUP  
apt-get autoremove && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
#RCLONE  
RUN \  
mkdir -p $BUILD_DIR && \  
cd $BUILD_DIR && \  
wget $RCLONE_URL -O rclone.zip -q && \  
unzip -j rclone.zip -d rclone && \  
mv rclone/rclone /usr/local/bin/ && \  
mv rclone/rclone.1 /usr/local/man && \  
cd ~ && \  
rm -rf $BUILD_DIR/rclone  
  
#ACDCLI  
RUN \  
pip3 install setuptools && \  
pip3 install --upgrade git+https://github.com/yadayada/acd_cli.git  
  
EXPOSE 22  
CMD ["/bin/sleep", "infinity"]

