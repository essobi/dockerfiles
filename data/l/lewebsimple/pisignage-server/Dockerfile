FROM ubuntu:xenial  
MAINTAINER Pascal Martineau <pascal@lewebsimple.ca>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install package dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl \  
ffmpeg \  
git \  
imagemagick \  
iputils-ping \  
nano \  
software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Node.js 8.x  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
# Clone repository and build  
COPY . /usr/src/app  
RUN cd /usr/src/app && npm install  
  
EXPOSE 3000  
WORKDIR /usr/src/app  
  
VOLUME ["/usr/src/app/data"]  
  
CMD ["/usr/src/app/scripts/docker-entrypoint.sh"]  

