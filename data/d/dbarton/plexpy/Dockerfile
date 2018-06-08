FROM debian:8  
MAINTAINER Dominique Barton  
  
#  
# Create user and group for PlexPy.  
#  
RUN groupadd -r -g 666 plexpy \  
&& useradd -r -u 666 -g 666 -d /plexpy plexpy  
  
#  
# Add PlexPy init script.  
#  
ADD plexpy.sh /plexpy.sh  
RUN chmod 755 /plexpy.sh  
  
#  
# Install PlexPy and all required dependencies.  
#  
RUN export VERSION=v1.4.25 \  
&& apt-get -q update \  
&& apt-get install -qy curl ca-certificates python-setuptools build-essential
python-dev libssl-dev \  
&& easy_install pip \  
&& curl -o /tmp/plexpy.tar.gz
https://codeload.github.com/JonnyWong16/plexpy/tar.gz/${VERSION} \  
&& tar xzf /tmp/plexpy.tar.gz \  
&& mv plexpy-* plexpy \  
&& chown -R plexpy: plexpy \  
&& pip install pyOpenSSL \  
&& apt-get -y remove curl build-essential python-dev libssl-dev \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
#  
# Define container settings.  
#  
EXPOSE 8181  
#  
# Start PlexPy.  
#  
WORKDIR /plexpy  
CMD ["/plexpy.sh"]  

