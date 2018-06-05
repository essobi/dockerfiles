FROM lanrat/filebot  
MAINTAINER Ian Foster <ian@vorsk.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
ffmpeg && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
#ENTRYPOINT ["/usr/bin/filebot"]  

