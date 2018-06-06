FROM openjdk:8-jre  
  
ENV SUBGIT_VERSION 3.2.4  
# Dependencies  
RUN ( apt-get update && \  
apt-get install -y git subversion wget incron sudo && \  
rm -rf /var/lib/apt/lists/* )  
  
# Download from official website and install  
RUN ( wget -O subgit.deb -q \  
\--header="User-Agent: Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.11 (KHTML,
like Gecko) Chrome/23.0.1271.97 Safari/537.11" \  
\--header="Referer: http://subgit.com/" \  
\--header="Accept-Encoding: compress, gzip" \  
https://subgit.com/download/subgit_${SUBGIT_VERSION}_all.deb && \  
dpkg -i subgit.deb && \  
rm -f subgit.deb )  
  
VOLUME /repo.git  
WORKDIR /repo.git  
  
ADD entrypoint.sh /  
ADD run-hook.sh /  
ENTRYPOINT /entrypoint.sh  
  

