FROM debian  
MAINTAINER jonathan lung <vapr@sojournlabs.com>  
RUN apt-get update  
RUN apt-get install -y \  
curl \  
gcc-4.7 \  
git \  
make  
RUN mkdir -p vapr  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.7 60  
ENV PATH /vapr:$PATH  
WORKDIR /vapr

