############################################################  
## ALUS AIRSPACE-CONVERTER DOCKER CONTAINER  
## See http://www.alus.it/AirspaceConverter and https://github.com/alus-
it/AirspaceConverter for  
## more details.  
############################################################  
  
FROM debian:jessie  
  
# prefix with DEBIAN_FRONTEND=noninteractive to avoid ugly warning messages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y --allow-
unauthenticated --no-install-recommends install \  
python-software-properties \  
software-properties-common \  
supervisor \  
wget \  
ca-certificates \  
openssl \  
libssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./supervisor.conf /etc/supervisor.conf  
  
# Add custom PPA keys and init supervisor  
RUN gpg --keyserver pgpkeys.mit.edu --recv-key BCDF65CBC85906AC && \  
gpg -a --export BCDF65CBC85906AC | apt-key add - && \  
add-apt-repository 'deb http://alus.altervista.org/debian/ jessie main' && \  
mkdir -p /var/log/supervisor  
  
# Update and install Alus airspace converter from custom PPA  
RUN apt-get update && apt-get install -y --no-install-recommends
airspaceconverter  
  
WORKDIR /  
  
# default command is to start the supervisord  
CMD ["supervisord", "-c", "/etc/supervisor.conf"]  

