FROM node:8.1  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
git \  
libssl-dev \  
make \  
openssl \  
openssh-client \  
python3 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version 0.27.0

