FROM node:8-alpine  
  
RUN apk --no-cache add \  
\--virtual builds-deps \  
git \  
ca-certificates \  
wget \  
bash \  
curl \  
tar \  
gnupg \  
python \  
build-base \  
yarn  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
RUN apk --no-cache del \  
ca-certificates \  
wget \  
bash \  
curl \  
tar \  
gnupg  
  
RUN rm -rf /root/.gnupg  
  
ENV PATH /root/.yarn/bin:$PATH  
  

