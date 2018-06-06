FROM "node:latest"  
RUN buildDeps="\  
ruby-compass \  
"\  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/*  

