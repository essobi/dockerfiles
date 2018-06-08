FROM debian:jessie  
MAINTAINER uochan  
  
RUN apt-get update && apt-get install -y --no-install-recommends octave && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["octave"]  

