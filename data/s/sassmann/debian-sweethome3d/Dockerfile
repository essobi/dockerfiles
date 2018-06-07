FROM debian:sid  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends sweethome3d
sweethome3d-furniture xfonts-scalable \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN adduser --disabled-password user --gecos "User"  
USER user  
ENV HOME /home/user  
ENV PULSE_SERVER unix:/tmp/pulse  
  
RUN mkdir -p /home/user/sh3d  
RUN mkdir -p /home/user/.eteks  
RUN mkdir -p /home/user/.java/.userPrefs/com/eteks/  
  
CMD ["sweethome3d"]  

