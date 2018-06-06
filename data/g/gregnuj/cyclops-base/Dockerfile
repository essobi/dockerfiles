FROM debian:stretch-slim  
  
LABEL MAINTAINER="Greg Junge <gregnuj@gmail.com>"  
# Install packages  
RUN apt-get update && apt-get install -y \  
curl \  
cron \  
git \  
openssl \  
socat \  
sudo \  
supervisor \  
vim \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

