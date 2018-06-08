FROM debian:stable-20170620  
  
RUN buildDeps='curl ca-certificates build-essential zlib1g-dev python cmake';
\  
set -ex; \  
apt-get update && apt-get install -y $buildDeps --no-install-recommends; \  
rm -rf /var/lib/apt/lists/*; \  
\  
mkdir /usr/src/kafkacat; \  
curl -SLs "https://github.com/edenhill/kafkacat/archive/master.tar.gz" | tar
-xzf - --strip-components=1 -C /usr/src/kafkacat; \  
cd /usr/src/kafkacat; \  
./bootstrap.sh; \  
mv ./kafkacat /usr/local/bin/; \  
\  
rm -rf /usr/src/kafkacat/tmp-bootstrap; \  
apt-get purge -y --auto-remove $buildDeps  
  
ENTRYPOINT ["kafkacat"]  

