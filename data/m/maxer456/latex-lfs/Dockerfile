FROM macjustice/git-lfs  
  
RUN apt-get update -q && \  
apt-get install -qy texlive-full latexmk && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
VOLUME ["/data"]  

