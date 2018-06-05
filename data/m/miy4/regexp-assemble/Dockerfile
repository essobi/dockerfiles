FROM gliderlabs/alpine:3.3  
  
RUN apk add \--no-cache perl \  
&& apk add \--no-cache \--virtual build-dependencies make curl \  
&& curl -L https://cpanmin.us/ -o cpanm \  
&& chmod +x cpanm \  
&& ./cpanm \--no-wget Regexp::Assemble \  
&& ./cpanm \--uninstall Test::Pod \  
&& rm -rf /root/.cpanm ./cpanm \  
&& apk del build-dependencies  

