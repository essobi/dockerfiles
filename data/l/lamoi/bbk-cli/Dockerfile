FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -O http://beta1.bredbandskollen.se/download/bbk-cli_0.3.8_amd64.deb \  
&& dpkg -i bbk-cli_0.3.8_amd64.deb  
ENTRYPOINT ["bbk_cli"]  

