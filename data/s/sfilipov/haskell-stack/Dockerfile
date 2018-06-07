FROM buildpack-deps:jessie  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 575159689BEFB442
&& \  
echo 'deb http://download.fpcomplete.com/debian jessie main' | tee
/etc/apt/sources.list.d/fpco.list && \  
apt-get update && apt-get install -y --no-install-recommends \  
stack \  
&& rm -rf /var/lib/apt/lists/*  

