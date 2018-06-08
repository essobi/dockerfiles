FROM ubuntu:14.04  
MAINTAINER Vimalkumar Velayudhan <vimalkumarvelayudhan@gmail.com>  
  
# Install prerequisite libraries and tools  
RUN apt-get update && apt-get -y install \  
ant build-essential gfortran ghc git libatlas-base-dev libatlas-dev \  
libbz2-dev libc6-i386 libfreetype6-dev libgsl0-dev libhdf5-serial-dev \  
liblapack-dev libmysqlclient18 libmysqlclient-dev libncurses5-dev libpng12-dev
\  
libreadline-dev libsqlite3-dev libssl-dev libxml2 libxslt1.1 libxslt1-dev \  
libzmq-dev mpich2 openjdk-6-jdk pkg-config python-dev python-pip \  
sqlite3 subversion swig tcl-dev tk-dev unzip zlib1g-dev \  
apt-transport-https openjdk-7-jdk  
  
# Install Qiime plus dependencies using pip  
# recent version of matplotlib has issues in generating plots with Qiime  
RUN pip install numpy && pip install h5py matplotlib==1.4.3 qiime  
  
# Install latest R package from CRAN  
RUN echo "deb https://cloud.r-project.org/bin/linux/ubuntu trusty/" | tee -a
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys E084DAB9 && \  
apt-get update && apt-get -y install r-base r-base-dev  
  
# Install required R packages  
RUN printf "\  
install.packages(c('ape', 'biom', 'optparse', 'RColorBrewer', 'randomForest',
'vegan'), repo='https://cloud.r-project.org/')\n\  
source('https://bioconductor.org/biocLite.R')\n\  
biocLite(c('DESeq2', 'metagenomeSeq'))\n\  
q()\n" > /tmp/deps.R  
  
RUN Rscript /tmp/deps.R  
  
# Use qiime-deploy to install all other dependencies  
RUN cd && git clone https://github.com/qiime/qiime-deploy.git && \  
git clone https://github.com/qiime/qiime-deploy-conf.git  
  
RUN cd ~/qiime-deploy && python qiime-deploy.py /opt/qiime_deps/ -f \  
~/qiime-deploy-conf/qiime-1.9.1/qiime.conf \  
\--force-remove-failed-dirs  
  
# create and set user for container  
RUN useradd -m -s /bin/bash qiime  
USER qiime  

