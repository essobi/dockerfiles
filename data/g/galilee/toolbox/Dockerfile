FROM debian:stretch  
LABEL maintainer="Stéphane BARON <sbaron@galilee.fr>"  
  
RUN apt-get update --quiet \  
&& apt-get install --no-install-recommends --yes \--quiet \  
ncftp \  
zip \  
p7zip-full \  
gzip \  
bzip2 \  
xz-utils \  
curl \  
wget \  
ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /root/.ssh  
COPY resources/ssh_config /root/.ssh/config  
  
COPY resources/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

