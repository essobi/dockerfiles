FROM debian:stable-slim  
MAINTAINER wraithfive  
ENV LANG C.UTF-8  
#  
# Create user and group for SABnzbd.  
#  
RUN groupadd -r -g 666 sabnzbd \  
&& useradd -l -r -u 666 -g 666 -d /sabnzbd sabnzbd  
  
#  
# Add SABnzbd init script.  
#  
ADD sabnzbd.sh /sabnzbd.sh  
RUN chmod 755 /sabnzbd.sh  
  
#  
# Install SABnzbd and all required dependencies.  
#  
RUN export SABNZBD_VERSION=2.3.4 PAR2CMDLINE_VERSION=0.8.0 \  
&& sed -i "s/ main$/ main contrib non-free/" /etc/apt/sources.list \  
&& apt-get -q update \  
&& apt-get install -qy curl ca-certificates python-cheetah python-openssl
python-yenc python-dev python-pip unzip unrar p7zip-full build-essential
automake libgomp1 \  
&& pip install sabyenc --upgrade \  
&& curl -L -o /tmp/sabnzbd.tar.gz
https://github.com/sabnzbd/sabnzbd/releases/download/${SABNZBD_VERSION}/SABnzbd-${SABNZBD_VERSION}-src.tar.gz
\  
&& tar xzf /tmp/sabnzbd.tar.gz \  
&& mv SABnzbd-* sabnzbd \  
&& chown -R sabnzbd: sabnzbd \  
&& curl -L -o /tmp/par2cmdline.tar.gz
https://github.com/Parchive/par2cmdline/releases/download/v${PAR2CMDLINE_VERSION}/par2cmdline-${PAR2CMDLINE_VERSION}.tar.gz
\  
&& tar xzf /tmp/par2cmdline.tar.gz -C /tmp \  
&& cd /tmp/par2cmdline-* \  
&& aclocal \  
&& automake --add-missing \  
&& autoconf \  
&& ./configure \  
&& make \  
&& make install \  
&& apt-get -y remove curl build-essential automake \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd / \  
&& rm -rf /tmp/*  
  
#  
# Define container settings.  
#  
VOLUME ["/datadir", "/media", "/backup", "/watched"]  
  
EXPOSE 8080  
#  
# Start SABnzbd.  
#  
WORKDIR /sabnzbd  
  
CMD ["/sabnzbd.sh"]  

