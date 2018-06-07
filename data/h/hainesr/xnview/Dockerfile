#  
# Dockerfile for XnView MP.  
#  
# Robert Haines.  
#  
# BSD Licenced. See LICENCE for details.  
#  
FROM debian:sid  
MAINTAINER Robert Haines <robert.haines@manchester.ac.uk>  
  
ENV HOME /home/xnview  
  
RUN apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -qy \  
libfontconfig1 \  
libfreetype6 \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libglib2.0-0 \  
libgstreamer0.10-0 \  
libgstreamer-plugins-base0.10-0 \  
libpulse0 \  
libx11-6 \  
libxcomposite1 \  
libxml2 \  
libxrender1 \  
libxslt1.1 \  
xkb-data \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd --create-home --home-dir $HOME \--gid users xnview \  
&& mkdir -p $HOME/pics \  
&& chown -R xnview:users $HOME  
  
ADD http://download.xnview.com/XnViewMP-linux-x64.tgz /opt/xnview.tgz  
COPY entrypoint.sh /opt/  
  
RUN cd /opt \  
&& tar xzf xnview.tgz \  
&& rm -f xnview.tgz \  
&& chown -R xnview:users /opt  
  
WORKDIR $HOME/pics  
USER xnview  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  

