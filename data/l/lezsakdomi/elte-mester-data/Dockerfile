FROM debian  
  
# First install CircleCI tools  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git ssh tar gzip ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bash make curl gnupg2 \  
md5deep \  
poppler-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
ARG NODE_VERSION=9.x  
RUN curl -sL https://deb.nodesource.com/setup_$NODE_VERSION | bash -  
RUN apt-get update && apt-get install -y --no-install-recommends \  
nodejs \  
&& rm -rf /var/lib/apt/lists/*

