FROM debian:jessie  
  
RUN apt-get update && apt-get install -y make gcc patch ruby ruby-dev libxml2
zlib1g-dev git curl nodejs rsync \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc" \  
&& gem install jekyll html-proofer \  
&& apt-get purge -y \--auto-remove make gcc patch ruby-dev libxml2 zlib1g-dev  

