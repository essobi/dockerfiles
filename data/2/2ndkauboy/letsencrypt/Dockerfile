FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install git -y  
  
RUN git clone https://github.com/letsencrypt/letsencrypt && cd letsencrypt &&
./letsencrypt-auto --help && ln -s /letsencrypt/letsencrypt-auto
/usr/local/bin/letsencrypt-auto  
  
RUN apt-get autoremove -y git \  
&& rm -rf /var/lib/apt/lists/*

