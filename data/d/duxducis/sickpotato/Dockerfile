FROM debian:jessie  
  
# Install add-apt-repository  
RUN apt-get update  
  
# Install packages  
RUN apt-get update && apt-get install -y \  
git-core \  
python \  
wget \  
build-essential \  
python-dev \  
libffi-dev \  
libssl-dev \  
python-lxml \  
ruby \  
polipo  
  
RUN gem install tiller  
  
WORKDIR /tmp  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py && rm get-pip.py  
  
RUN pip install --upgrade pyopenssl ndg-httpsclient pyasn1 cffi cryptography
pycparser  
  
# Set nobody id and gid to match unraid  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
# Set the entry point  
ENTRYPOINT ["/init"]  
  
EXPOSE 5050 8081  
VOLUME /config/sickrage /config/couchpotato /tvshows /movies /kids/tvshows
/kids/movies /blackhole/sickrage /blackhole/couchpotato /complete/sickrage
/complete/couchpotato  
  
# Install services  
COPY services /etc/services.d  
  
# Install init.sh as init script  
COPY init.sh /etc/cont-init.d/  
  
# Copy tiller configuration  
COPY data /etc/tiller  
  
#RUN touch /etc/services.d/couchpotato/down  
#RUN touch /etc/services.d/sickrage/down  
#RUN touch /etc/services.d/polipo/down  
# Download and extract s6 init  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.10.0.3/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  

