# https://github.com/rclasen/srmio  
FROM debian:jessie  
  
# Install updates & dependencies  
RUN apt-get update && apt-get -qq dist-upgrade && apt-get install -y --no-
install-recommends \  
build-essential \  
automake \  
libtool \  
fakeroot \  
dh-make \  
git \  
&& apt-get clean  
  
# Install srmio  
RUN git clone git://github.com/rclasen/srmio /opt/srmio \  
&& cd /opt/srmio \  
&& sh genautomake.sh \  
&& fakeroot debian/rules binary \  
&& dpkg --install ../srmio_*.deb  
  
# Volume for data exchange  
VOLUME ["/data"]  
WORKDIR "/data"  
  
# srmcmd, srmdump, srmsync? pick one :)  

