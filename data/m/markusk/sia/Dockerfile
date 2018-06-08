FROM debian  
  
ARG SIA_VERSION=1.3.2  
RUN apt-get update && \  
apt-get install -y wget unzip && \  
mkdir -p /sia && \  
wget -O /tmp/sia.zip
https://github.com/NebulousLabs/Sia/releases/download/v$SIA_VERSION/Sia-v$SIA_VERSION-
linux-amd64.zip && \  
unzip -d /tmp/sia/ /tmp/sia.zip && \  
mv /tmp/sia/Sia-v$SIA_VERSION-linux-amd64/siac /usr/local/bin/ && \  
mv /tmp/sia/Sia-v$SIA_VERSION-linux-amd64/siad /usr/local/bin/ && \  
rm -rf /tmp/sia/ /tmp/sia.zip /var/lib/apt/lists  
  
WORKDIR /sia  
EXPOSE 9981 9982  
CMD ["/usr/local/bin/siad"]  

