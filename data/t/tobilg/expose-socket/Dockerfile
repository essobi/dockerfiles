FROM ubuntu:14.04.3  
MAINTAINER tobilg <fb.tools.github@gmail.com>  
  
# packages  
RUN apt-get update && apt-get install -yq --no-install-recommends --force-yes
\  
socat && \  
rm -rf /var/lib/apt/lists/*  
  
ADD start.sh .  
  
RUN chmod +x start.sh  
  
ENTRYPOINT ["/start.sh"]

