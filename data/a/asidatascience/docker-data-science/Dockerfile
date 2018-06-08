FROM ubuntu:16.10  
LABEL name=docker-data-science version=latest  
  
COPY ["requirements-conda.txt", "/"]  
  
ENV ANACONDA_VERSION 4.3.0  
ENV PATH /opt/anaconda/bin:${PATH}  
  
RUN apt-get update -qq && \  
env DEBIAN_FRONTEND=noninteractive apt-get install -qq \  
bzip2 curl libglib2.0-0 libxext6 libsm6 libxrender1 && \  
curl -sLO https://repo.continuum.io/archive/Anaconda3-$ANACONDA_VERSION-
Linux-x86_64.sh && \  
echo
"090037d4734a5351276ca0a15922f98f6074a504a56213ac541148a580216d768894d70d5ac1a7f5c1e6997368abe91e65e8dc400a024b72407042d067c0543e
Anaconda3-$ANACONDA_VERSION-Linux-x86_64.sh" | sha512sum -c && \  
bash Anaconda3-$ANACONDA_VERSION-Linux-x86_64.sh -b -p /opt/anaconda && \  
rm Anaconda3-$ANACONDA_VERSION-Linux-x86_64.sh && \  
conda update --all -qy && \  
conda install -qy --file /requirements-conda.txt && \  
rm /requirements-conda.txt && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* /root/.cache/pip && \  
conda clean -y --all  
  
VOLUME /var/jupyter  
  
WORKDIR /var/jupyter  
  
EXPOSE 8888  
CMD env SHELL=/bin/bash jupyter notebook --ip=0.0.0.0 --no-browser --port=8888  

