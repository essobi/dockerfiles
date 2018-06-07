################## BASE IMAGE ######################  
FROM ubuntu:17.10  
################## METADATA ######################  
LABEL base.image="ubuntu:17.10"  
LABEL pipeline="tuxedo2"  
LABEL name="tuxedo2_pipeline_worker"  
LABEL description="Docker image containing all required packages to run new
Tuxedo differential expression analysis protocol"  
LABEL website="https://ccb.jhu.edu/software/hisat2/index.shtml"  
LABEL
documentation="https://ccb.jhu.edu/software/stringtie/index.shtml?t=manual#de"  
LABEL license="GPL-2.0"  
LABEL tags="Genomics"  
LABEL maintainer="Ilya Vasilyev <u0412u0418u042e@gmail.com>"  
  
################## INSTALLATION ######################  
# Base image CLI: docker run --rm -it ubuntu:17.10 bash  
# Enable apt-get noninteractive install  
ENV DEBIAN_FRONTEND noninteractive  
  
# Software update  
RUN apt-get clean all && \  
apt-get -y update && \  
apt-get -y upgrade  
  
RUN apt-get -y install \  
curl \  
python \  
python-pip \  
wget \  
tar \  
zip \  
bzip2 \  
ca-certificates \  
libglib2.0-0 \  
libxext6 \  
libsm6 \  
libxrender1 \  
git \  
mercurial \  
subversion  
  
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
  
# Install Conda - a cross-platform, language-agnostic binary package manager  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet 'https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh' -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
# Install Python packages  
RUN for p in numpy scipy pandas redis; do pip install ${p}; done  
  
# Create user docker with password docker  
RUN groupadd fuse && \  
useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups
sudo,fuse docker && \  
echo `echo "docker\ndocker\n" | passwd docker` && \  
mkdir /data /config ${REF_DIR} && \  
chown docker:docker /data /config ${REF_DIR} && \  
chmod -R 755 /data /config ${REF_DIR}  
  
# Give ultimate access to the Conda directory  
RUN chmod 777 -R /opt/conda  
  
# Change user (CLI: su - docker)  
USER docker  
  
# Update Path variables  
ENV PATH=$PATH:/opt/conda/bin  
ENV PATH=$PATH:/home/docker/bin  
ENV HOME=/home/docker  
  
# Setup Conda  
RUN conda config --add channels r && \  
conda config --add channels bioconda && \  
conda config --add channels biobuilds && \  
conda config --add channels intel && \  
conda upgrade -y conda  
  
# Install additional Conda packages  
RUN for c in "intel tbb" "biobuilds ncbi-ngs-sdk" "bioconda sra-tools"
"bioconda hisat2" "bioconda samtools" "bioconda stringtie" "bioconda
gffcompare"; do conda install -y -c ${c} && conda upgrade -y -c ${c}; done  
  
# Get the pipeline scripts  
RUN mkdir ~/scripts && \  
cd ~/scripts && \  
git clone https://github.com/ivasilyev/biopipelines-docker.git && \  
mv biopipelines-docker/tuxedo2_pipeline/worker/pipeline_wrapper.py . && \  
rm -rf bowtie-tools biopipelines-docker && \  
chmod -R +x ~/scripts && \  
echo "export PATH=$PATH:${PWD}" | tee -a ~/.bashrc  
  
# Directories to mount  
VOLUME ["/data", "/config", "/reference"]  
  
# Overwrite this with 'CMD []' in a dependent Dockerfile  
# CMD ["/bin/bash"]  
CMD ["python", "/home/docker/scripts/pipeline_wrapper.py"]  
  
# Setup the default directory  
WORKDIR /home/docker  
  
# Manual build command: docker build -t tuxedo2_pipeline_worker . && docker
tag tuxedo2_pipeline_worker ivasilyev/tuxedo2_pipeline_worker:latest && docker
push ivasilyev/tuxedo2_pipeline_worker:latest  

