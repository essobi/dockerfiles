FROM ubuntu:16.04  
LABEL author="Kersten Breuer, Zeller Team, EMBL 2017" \  
maintainer="kersten-breuer@outlook.com"  
  
# Install essential unix packages and dependencies:  
RUN apt-get update -y --fix-missing  
RUN apt-get install -y build-essential \  
wget \  
tar \  
make \  
python-dev \  
python-pip \  
zlib1g-dev \  
g++ \  
bc  
  
# Install Megahit:  
ENV MEGAHIT_URL https://github.com/voutcn/megahit/archive/v1.1.2.tar.gz  
RUN cd /usr/local/ \  
&& wget -O megahit.tar.gz ${MEGAHIT_URL} \  
&& tar -xvzf megahit.tar.gz \  
&& rm megahit.tar.gz \  
&& mv megahit* megahit \  
&& cd megahit \  
&& make  
ENV PATH="/usr/local/megahit/:${PATH}"  
CMD ["megahit"]

