FROM bmoorman/ubuntu:xenial  
  
ARG DEBIAN_FRONTEND="noninteractive"  
WORKDIR /opt  
  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends \  
curl \  
jq \  
libmono-cil-dev \  
libcurl3 \  
mediainfo \  
&& fileUrl=$(curl --silent --location
"https://api.github.com/repos/Radarr/Radarr/releases" | jq --raw-output '[.[]
| select(.prerelease == true)][0].assets[] | select(.name | contains("linux"))
| .browser_download_url') \  
&& curl --silent --location "${fileUrl}" | tar xz \  
&& apt-get autoremove --yes --purge \  
&& apt-get clean \  
&& rm --recursive --force /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY radarr/ /etc/radarr/  
  
VOLUME /config  
  
EXPOSE 7878  
CMD ["/etc/radarr/start.sh"]  
  
HEALTHCHECK \--interval=60s --timeout=5s CMD curl --silent --location --fail
http://localhost:7878/ > /dev/null || exit 1  

