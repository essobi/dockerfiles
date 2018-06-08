FROM bmoorman/ubuntu:xenial  
  
ARG DEBIAN_FRONTEND="noninteractive"  
WORKDIR /opt  
  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends \  
curl \  
jq \  
&& fileUrl=$(curl --silent --location
"https://api.github.com/repos/Portainer/Portainer/releases" | jq --raw-output
'[.[] | select(.prerelease == false)][0].assets[] | select(.name |
contains("linux-amd64")) | .browser_download_url') \  
&& curl --silent --location "${fileUrl}" | tar xz \  
&& apt-get autoremove --yes --purge \  
&& apt-get clean \  
&& rm --recursive --force /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY portainer/ /etc/portainer/  
  
VOLUME /config  
  
EXPOSE 9000  
CMD ["/etc/portainer/start.sh"]  
  
HEALTHCHECK \--interval=60s --timeout=5s CMD curl --silent --location --fail
http://localhost:9000/ > /dev/null || exit 1  

