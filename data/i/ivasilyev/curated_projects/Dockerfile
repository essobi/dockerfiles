FROM ubuntu:18.04  
# CLI: docker pull ubuntu:18.04 && docker run --rm -v /data:/data -v
/data1:/data1 -v /data2:/data2 -it debian:jessie bash  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install \  
# Base packets  
ca-certificates \  
curl \  
python3 \  
python3-pip \  
# Required by lxml  
libxml2-dev \  
libxslt1-dev \  
zlib1g-dev \  
# Required by matplotlib  
python3-tk  
  
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
RUN pip3 install \  
# For 'tgrigoreva/25_ecoli_genes' project  
pandas matplotlib statsmodels scipy requests bs4 lxml jinja2 pyyaml \  
# For 'ndanilova/colitis_crohn/SCFAs_from_KEGG' project  
xlrd  
  
  
# Create user docker with password docker  
RUN groupadd fuse && \  
useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups
sudo,fuse docker && \  
echo `echo "docker\ndocker\n" | passwd docker` && \  
mkdir /data /config ${REF_DIR} && \  
chown docker:docker /data /config ${REF_DIR} && \  
chmod -R 755 /data /config ${REF_DIR}  
  
# Change user (CLI: su - docker)  
USER docker  
  
# Update environment variables  
ENV PATH=$PATH:/home/docker/bin  
ENV HOME=/home/docker  
WORKDIR /home/docker  
  
CMD ["/bin/bash"]  
  
# MANUAL BUILD COMMAND:  
# export DOCKER_IMAGE_NAME=curated_projects && docker build -t
${DOCKER_IMAGE_NAME} . && docker tag ${DOCKER_IMAGE_NAME}
ivasilyev/${DOCKER_IMAGE_NAME}:latest && docker push
ivasilyev/${DOCKER_IMAGE_NAME}:latest  

