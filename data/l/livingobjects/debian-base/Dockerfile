FROM debian:9.2  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
ADD run-one /usr/bin/run-one  
  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
echo "APT::Install-Recommends \"0\";" > /etc/apt/apt.conf.d/no-recommends && \  
echo "APT::Install-Suggests \"0\";" >> /etc/apt/apt.conf.d/no-recommends && \  
echo "Dpkg::Options { \"--force-confdef\"; \"--force-confold\"; }" >>
/etc/apt/apt.conf.d/local && \  
# Install minimal packages  
apt-get -y update && apt-get install -y --no-install-recommends \  
sudo \  
vim \  
runit \  
wget \  
bzip2 \  
unzip \  
netcat \  
locales \  
ca-certificates \  
telnet \  
curl && \  
apt-get autoclean && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
# Set locale  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8 && \  
# Set timezone  
ln -sf /usr/share/zoneinfo/UTC /etc/localtime && \  
echo "Etc/UTC" > /etc/timezone && \  
# Create lo-daemon  
groupadd -g 999 lo-daemon && \  
useradd lo-daemon --uid 999 \--gid 999 \--system --home /services/ \--shell
/bin/bash && \  
gpasswd -a lo-daemon lo-daemon  
  
ENV LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8

