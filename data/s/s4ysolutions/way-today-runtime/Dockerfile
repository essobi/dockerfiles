# Set the base image to Ubuntu  
FROM s4ysolutions/nodejs8x  
  
# File Author / Maintainer  
MAINTAINER Sergey Dolin <sergey@s4y.solutions>  
RUN apt-get update \  
&& apt-get install -y curl \  
&& apt-get install -y libzmq-dev \  
&& apt-get install -y python \  
&& apt-get install -y make \  
&& apt-get install -y g++ \  
&& rm -rf /var/lib/apt/lists/*  

