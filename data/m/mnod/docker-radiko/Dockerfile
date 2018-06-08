From ubuntu:16.04  
RUN apt-get update && apt-get install --no-install-recommends -y \  
wget \  
rtmpdump \  
vlc-nox \  
swftools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
RUN useradd -s /bin/bash -m docker  
  
EXPOSE 8000  
USER docker  
ENTRYPOINT ["/run.sh"]  

