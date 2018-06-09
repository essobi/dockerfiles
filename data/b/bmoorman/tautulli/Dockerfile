FROM bmoorman/ubuntu:xenial  
  
ARG DEBIAN_FRONTEND="noninteractive"  
WORKDIR /opt  
  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends \  
curl \  
git \  
python \  
&& git clone https://github.com/Tautulli/Tautulli.git \  
&& apt-get autoremove --yes --purge \  
&& apt-get clean \  
&& rm --recursive --force /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY tautulli/ /etc/tautulli/  
  
VOLUME /config  
  
EXPOSE 8181  
CMD ["/etc/tautulli/start.sh"]  
  
HEALTHCHECK \--interval=60s --timeout=5s CMD curl --silent --location --fail
http://localhost:8181/ > /dev/null || exit 1  

