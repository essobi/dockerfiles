FROM debian:stretch-slim  
  
RUN set -ex \  
&& apt-get update \  
# http://ncmpcpp.rybczak.net/download.php#debian  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ncmpcpp \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
# Create a random UID to avoid running as root.  
&& useradd --uid 71723 -m ncmpcpp  
  
USER ncmpcpp  
  
CMD ["ncmpcpp"]  

