FROM golang:1.10  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
zip \  
tar \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
  

