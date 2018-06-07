FROM felixweis/buildpack-deps:jessie-boost  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libdb-dev \  
libdb++-dev \  
&& rm -rf /var/lib/apt/lists/*  

