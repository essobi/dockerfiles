FROM ubuntu:16.10  
  
RUN apt-get -y update && apt-get install -y \  
ant \  
build-essential \  
cmake \  
doxygen \  
default-jdk \  
figlet \  
maven \  
git-core \  
python-dev \  
python-numpy \  
python-tk \  
python3-dev \  
python3-numpy \  
python3-tk \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY assets/toolVersions.sh /  
RUN chmod +x /toolVersions.sh  
  
ENTRYPOINT ["bash", "/toolVersions.sh"]

