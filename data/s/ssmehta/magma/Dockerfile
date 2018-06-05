FROM ssmehta/rdkit:Release_2016_03_1  
MAINTAINER Sajjan Singh Mehta "sajjan.s.mehta@gmail.com"  
# Set home directory  
ENV HOME /root  
WORKDIR /root  
  
# Download dependencies  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y libxml2-dev libxslt-dev libz-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install python dependencies  
RUN wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py && \  
pip install -U pip setuptools cython pp  
  
# Clone MAGMa repo  
RUN cd /root && \  
git clone https://github.com/NLeSC/MAGMa.git && \  
cd /root/MAGMa && \  
git reset \--hard 05f4798e0c49905e137005186ced962f528bb8f8 && \  
git submodule update \--init  
# Build MAGMa  
RUN cd /root/MAGMa/job && \  
python setup.py develop  
  
# Set entrypoint  
ENTRYPOINT ["./docker_entrypoint.sh"]  

