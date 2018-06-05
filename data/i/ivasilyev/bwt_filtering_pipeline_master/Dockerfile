################## BASE IMAGE ######################  
FROM redis  
  
################## METADATA ######################  
LABEL base.image="ubuntu:17.10"  
LABEL pipeline="bwt_filtering"  
LABEL name="bwt_filtering_pipeline_master"  
LABEL description="Docker image to manage the corresponding pipeline queue
using Redis & k8s features"  
LABEL website="https://github.com/ivasilyev/bowtie-tools"  
LABEL documentation="https://github.com/ivasilyev/ThreeBees"  
LABEL license="GPL-2.0"  
LABEL tags="Genomics"  
LABEL maintainer="Ilya Vasilyev <u0412u0418u042e@gmail.com>"  
  
################## INSTALLATION ######################  
# Base image CLI:  
# Enable apt-get noninteractive install  
ENV DEBIAN_FRONTEND noninteractive  
  
# Software update  
RUN apt-get clean all && \  
apt-get -y --force-yes update && \  
apt-get -y --force-yes upgrade  
  
# Software installation  
RUN apt-get -y --force-yes install \  
git \  
fuse \  
python3 \  
python3-pip \  
dpkg \  
curl  
  
# Install Tini - A tiny but valid init for containers  
RUN TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep
-o "/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb  
  
# Cleanup  
RUN apt-get clean && \  
apt-get purge && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Python packages  
RUN pip3 install redis  
  
# Create user docker with password docker  
RUN groupadd fuse && \  
useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups
sudo,fuse docker && \  
echo `echo "docker\ndocker\n" | passwd docker` && \  
chown docker:docker /data && \  
chmod -R 777 /data  
  
# Change user (CLI: su - docker)  
USER docker  
  
# Update Path variables  
ENV HOME=/home/docker  
  
# Get the pipeline scripts  
RUN mkdir ~/scripts ~/bin && \  
cd ~/scripts && \  
git clone https://github.com/ivasilyev/biopipelines-docker.git && \  
mv biopipelines-docker/bwt_filtering_pipeline/master/sampledata2jsons_queue.py
. && \  
rm -rf biopipelines-docker && \  
chmod -R +x ~/scripts && \  
echo "export PATH=$PATH:${PWD}" | tee -a ~/.bashrc  
  
# Overwrite this with 'CMD []' in a dependent Dockerfile  
# CMD ["/bin/bash"]  
CMD ["python3", "/home/docker/scripts/sampledata2jsons_queue.py"]  
  
# Setup the default directory  
WORKDIR /home/docker  
  
# MANUAL BUILD COMMAND:  
# docker build -t bwt_filtering_pipeline_master . && docker tag
bwt_filtering_pipeline_master ivasilyev/bwt_filtering_pipeline_master:latest
&& docker push ivasilyev/bwt_filtering_pipeline_master:latest  

