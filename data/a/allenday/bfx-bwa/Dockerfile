FROM ubuntu:12.04  
MAINTAINER Allen Day "allenday@allenday.com"  
ENV IMAGE_PACKAGES="samtools picard-tools"  
ENV BUILD_PACKAGES="make gcc wget zlib1g-dev"  
RUN apt-get -y update  
RUN apt-get -y --no-install-recommends install $BUILD_PACKAGES $IMAGE_PACKAGES  
  
WORKDIR /tmp  
RUN wget --no-check-certificate
https://github.com/lh3/bwa/archive/v0.7.15.tar.gz  
RUN tar -xvzf v0.7.15.tar.gz  
WORKDIR /tmp/bwa-0.7.15  
RUN make  
RUN cp ./bwa /usr/bin/  
RUN cp ./*.pl /usr/bin/  
  
## cleanup  
RUN apt-get -y remove --purge $BUILD_PACKAGES  
RUN apt-get -y remove --purge $(apt-mark showauto)  
RUN rm -rf /var/lib/apt/lists/*  

