FROM bmoorman/ubuntu:xenial  
  
ARG DEBIAN_FRONTEND="noninteractive"  
WORKDIR /opt/Ombi  
  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends \  
curl \  
jq \  
libcurl3 \  
libicu55 \  
libunwind8 \  
&& fileUrl=$(curl --silent --location
"https://api.github.com/repos/tidusjar/Ombi/releases" | jq --raw-output '[.[]
| select(.prerelease == false)][0].assets[] | select(.name == "linux.tar.gz")
| .browser_download_url') \  
&& curl --silent --location "${fileUrl}" | tar xz \  
&& apt-get autoremove --yes --purge \  
&& apt-get clean \  
&& rm --recursive --force /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ombi/ /etc/ombi/  
  
VOLUME /config  
  
EXPOSE 5000  
CMD ["/etc/ombi/start.sh"]  
  
HEALTHCHECK \--interval=60s --timeout=5s CMD curl --silent --location --fail
http://localhost:5000/ > /dev/null || exit 1  

