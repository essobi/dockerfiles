# Run ChromeDriver in a container  
#  
# docker run --rm \  
# --init \  
# -v /dev/shm:/dev/shm \  
# -p 9515:9515 \  
# --name chromedriver \  
# akirakoyasu/chromedriver \  
# --whitelisted-ips \  
# --verbose  
#  
FROM jess/chrome  
LABEL maintainer="Akira Koyasu <mail@akirakoyasu.net>"  
  
ARG CHROMEDRIVER_VERSION=2.33  
USER root  
# Fix duplication  
RUN rm /etc/apt/sources.list.d/google.list  
# Install chromedriver  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
unzip \  
\--no-install-recommends \  
&& curl -sSL -O
https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip
\  
&& unzip chromedriver_linux64.zip \  
&& chmod +x chromedriver \  
&& mv -f chromedriver /usr/local/share/chromedriver \  
&& ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver \  
&& rm -f chromedriver_linux64.zip \  
&& apt-get purge --auto-remove -y curl unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
USER chrome  
ENTRYPOINT [ "chromedriver" ]  
CMD []  

