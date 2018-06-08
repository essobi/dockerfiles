FROM ubuntu:14.04  
# Some common optimizations for ubuntu under docker  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
ENV HOME=/root \  
DEBIAN_FRONTEND=noninteractive \  
INITRD=No  
  
# Ensure Apt assumes -y, installs as little as possible, don't use cache, and
cleans up after itself  
RUN echo -e '\  
\rAPT::Install-Recommends "false";\n \  
\rAPT::Install-Suggests "false";\n \  
\rAPT::Get::Assume-Yes "true";\n \  
\rAPT::Get::Force-Yes "true"; \  
' >/etc/apt/apt.conf.d/01-auto-minimal &&\  
echo -e '\  
\rDir::Cache { srcpkgcache ""; pkgcache ""; };\n \  
\rDPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb || true";}; \  
' > /etc/apt/apt.conf.d/02no-cache &&\  
echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' >
/etc/apt/apt.conf.d/02compress-indexes &&\  
echo 'force-unsafe-io' | tee /etc/dpkg/dpkg.cfg.d/02apt-speedup &&\  
dpkg-divert --local \--rename /usr/bin/ischroot && ln -sf /bin/true
/usr/bin/ischroot &&\  
# Install node using ppa  
apt-get install software-properties-common &&\  
add-apt-repository -y ppa:chris-lea/node.js &&\  
apt-get update &&\  
apt-get update && apt-get dist-upgrade &&\  
apt-get install nodejs &&\  
# Firefox  
apt-get install default-jre git firefox  
  
# Chrome  
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo
apt-key add - \  
# sudo bash -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main"
>> /etc/apt/sources.list.d/google.list' \  
# apt-get -q update \  
# apt-get -qy install google-chrome-stable  
# Headless  
RUN apt-get install xvfb libgl1-mesa-dri xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic &&\  
# Install sitespeed.io using npm comming from .deb  
mkdir ~/.npm &&\  
npm install -g sitespeed.io &&\  
# Clean up APT when done.  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /results  
ADD xvfb.sh /root/xvfb.sh  
RUN chmod +x /root/xvfb.sh  
ENV DISPLAY :1  
ENTRYPOINT ["/root/xvfb.sh"]  

