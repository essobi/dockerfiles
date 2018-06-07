FROM andronics/mono:debian-jessie-slim  
  
LABEL author="andronics <andronics@gmail.com>"  
  
ENV XDG_DATA_HOME="/app/config"  
ENV XDG_CONFIG_HOME="/app/config"  
RUN apt-get update && \  
apt-get install -y curl libmono-cil-dev && \  
jack_tag=$(curl -sX GET
"https://api.github.com/repos/Jackett/Jackett/releases/latest" | awk
'/tag_name/{print $4;exit}' FS='[""]') && \  
curl -o /tmp/jacket.tar.gz -L
https://github.com/Jackett/Jackett/releases/download/$jack_tag/Jackett.Binaries.Mono.tar.gz
&& \  
mkdir -p /opt/jackett && \  
tar xf /tmp/jacket.tar.gz -C /opt/jackett --strip-components=1 && \  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* && \  
useradd -U -r -s /bin/false jackett  
  
COPY rootfs/ /  

