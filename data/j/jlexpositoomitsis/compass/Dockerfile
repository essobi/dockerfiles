FROM ubuntu:16.04  
  
RUN set -xe \  
&& buildDeps=" \  
ruby \  
ruby-dev \  
build-essential \  
" \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \  
&& gem install compass \  
#Reduce image size  
&& rm -rf /tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
#Add user compass and assign UID 1000  
RUN useradd -r -g www-data -u 1000 compass -d /var/www/html \  
&& chown -R compass:www-data /var/lib/gems/  
  
USER compass  
WORKDIR /var/www/html/  
ENTRYPOINT ["compass"]

