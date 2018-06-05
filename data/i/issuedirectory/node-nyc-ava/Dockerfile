FROM node:8  
  
RUN echo "Caching NPM files" \  
&& npm cache add nyc \  
&& npm cache add ava \  
&& apt-get update \  
&& apt-get install -y \  
make gcc g++ python \  
git \  
&& rm -rf /var/lib/apt/lists/* \  
&& npm cache add bower \  
&& npm cache add sinon \  
&& npm cache add express \  
&& echo "Finished caching files."  

