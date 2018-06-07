FROM ubuntu:latest  
MAINTAINER Christopher Emerson <christopher.emerson@whiteoaksecurity.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
git \  
wget \  
phantomjs \  
&& rm -rf /var/lib/apt/lists/*  
RUN git clone https://github.com/ChrisTruncer/EyeWitness.git  
  
RUN mkdir /output  
VOLUME ["/output"]  
WORKDIR /EyeWitness/setup  
  
RUN ./setup.sh  
  
WORKDIR /EyeWitness/  
ENTRYPOINT ["python", "EyeWitness.py"]  

