FROM ubuntu:17.10  
  
MAINTAINER Laurent Jourdren <jourdren@biologie.ens.fr>  
  
RUN apt update && \  
DEBIAN_FRONTEND=noninteractive apt install --yes \  
python3 \  
python3-pip\  
git\  
python3-tk\  
python3-h5py\  
python3-matplotlib\  
python3-pandas\  
python3-numpy\  
python3-seaborn && \  
pip3 install --upgrade setuptools && \  
cd /tmp && \  
git clone https://github.com/GenomicParisCentre/toulligQC && \  
cd toulligQC && \  
git checkout v0.9 && \  
python3 setup.py build install && \  
apt remove --yes git && \  
apt clean  
ENTRYPOINT ["toulligqc"]  
CMD ["--help"]  

