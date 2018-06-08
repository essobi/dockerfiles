FROM debian:stretch  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y \--no-install-recommends wget gnupg2 ca-certificates && \  
echo deb http://packages.prosody.im/debian stretch main | tee -a
/etc/apt/sources.list && \  
wget https://prosody.im/files/prosody-debian-packages.key -O- | apt-key add \-
&& \  
apt-get update && \  
apt-get install -y \--no-install-recommends prosody lua-event lua-sec lua-
bitop lua-zlib && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir /var/run/prosody && chown prosody:prosody /var/run/prosody  
  
EXPOSE 5222 5223 5269 5347 5280  
  
USER prosody  
CMD prosody  

