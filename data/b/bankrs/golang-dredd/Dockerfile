# This image adds tools only needed for testing  
FROM golang:1.10.2-stretch  
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \  
&& apt-get -y upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs \  
&& npm install -g --unsafe-perm --loglevel warn --user 0 \--no-progress
dredd@5.1.8 \  
&& rm -rf /var/lib/apt/lists/*  

