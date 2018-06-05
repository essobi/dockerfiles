# alvaroreig/theeconomist2kindle-amd64  
FROM ubuntu  
MAINTAINER Alvaro Reig "alvaroreig@gmail.com"  
RUN \  
  
# Install dependencies.  
  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive PYTHONIOENCODING="utf-8" apt-get install --no-
install-recommends -y $(apt-cache depends calibre | grep Depends | sed
"s/.*ends:\ //" | tr '\n' ' ') && \  
DEBIAN_FRONTEND=noninteractive PYTHONIOENCODING="utf-8" apt-get install --no-
install-recommends -y sudo ca-certificates wget python xz-utils xdg-utils && \  
  
# Using Calibre script  
  
sudo -v && wget --no-check-certificate -nv -O- https://download.calibre-
ebook.com/linux-installer.py | sudo python -c "import sys;
main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read());
main()" && \  
# Cleaning up  
apt-get -y autoremove && apt-get clean && \  
apt-get purge && \  
rm -rf rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY the_economist_to_kindle.sh the_economist_to_kindle.sh  
  
# Assuming that the env vars are passed on runtime, this command sends
Pocket's content to Kindle.  
ENTRYPOINT /bin/bash the_economist_to_kindle.sh

