# qa-dkrz  
#  
FROM continuumio/miniconda  
MAINTAINER https://github.com/IS-ENES-Data/QA-DKRZ  
  
LABEL Description="Quality Assurance Tool by DKRZ" Vendor="DKRZ"
Version="0.5.0"  
  
# Prepare system  
RUN apt-get update && apt-get install -y vim tmux byobu libuuid1 uuid-dev
libkeyutils1  
  
# Update conda  
RUN conda update -y -q conda  
  
# Add additional conda channels  
RUN conda config --add channels birdhouse  
  
# Install qa-dkrz and other useful packages  
RUN conda install -y -c birdhouse qa-dkrz cdo  
  
# Add user hdh  
#RUN useradd -d /home/hdh -m hdh  
# Remaining tasks run as user hdh  
#USER hdh  
# Change to user home  
#WORKDIR /home/hdh  
WORKDIR /root  
  
# Set conda env  
#RUN conda create -y -q -n qa-dkrz -c birdhouse python=2.7  
#RUN source activate qa-dkrz  
# add mount point for data  
VOLUME /data  
  
# Start with byobu session  
CMD ["byobu"]  
  

