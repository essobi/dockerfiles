FROM ubuntu  
  
RUN ["/bin/bash", "-c", "set -eo pipefail \  
&& apt-get update \  
&& apt-get install --yes \  
curl \  
&& echo 'deb https://crawl.develz.org/debian crawl 0.21' | tee -a
/etc/apt/sources.list \  
&& curl --silent https://crawl.develz.org/debian/pubkey | apt-key add - \  
&& apt-get install --yes crawl \  
&& rm -rf /var/lib/apt/lists/*"]  
  
RUN useradd --create-home crawl  
  
WORKDIR /home/crawl  
USER crawl  
  
ENTRYPOINT ["/usr/games/crawl"]  

