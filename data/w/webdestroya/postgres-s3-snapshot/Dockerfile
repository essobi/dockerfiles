FROM debian:jessie  
  
MAINTAINER Mitch Dempsey <mitch@mitchdempsey.com>  
  
RUN apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy --no-install-recommends install \  
curl \  
postgresql-client-common \  
postgresql-client \  
python-pip && \  
pip install awscli && \  
apt-get -qy clean autoclean autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# Volume for a larger scratch drive?  
COPY snapshot.sh /snapshot.sh  
  
ENTRYPOINT ["/bin/bash"]  
  
CMD ["/snapshot.sh"]  

