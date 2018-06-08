# Creates docker container that runs HCP Pipeline algorithms  
#  
#  
# Use Ubuntu 14.04 LTS  
FROM ubuntu:trusty-20170817  
MAINTAINER Flywheel <support@flywheel.io>  
  
# Install packages  
RUN apt-get update \  
&& apt-get install -y \  
lsb-core \  
bsdtar \  
zip \  
unzip \  
gzip \  
curl \  
jq \  
python-pip  
  
#############################################  
# Download and install R and necessary packages  
#From https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIX/UserGuide  
#R version >=3.3.0  
#'kernlab' version 0.9.24  
#'ROCR' version 1.0.7  
#'class' version 7.3.14  
#'party' version 1.0.25  
#'e1071' version 1.6.7  
#'randomForest' version 4.6.12  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \  
echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list.d/cran-rstudio.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends r-base-core=3.3.1-* r-base-
dev=3.3.1-* && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e 'install.packages("kernlab", dependencies=TRUE)'  
RUN Rscript -e 'install.packages("ROCR", dependencies=TRUE)'  
RUN Rscript -e 'install.packages("class", dependencies=TRUE)'  
RUN Rscript -e 'install.packages("party", dependencies=TRUE)'  
RUN Rscript -e 'install.packages("e1071", dependencies=TRUE)'  
RUN Rscript -e 'install.packages("randomForest", dependencies=TRUE)'  
RUN Rscript -e
'install.packages("https://cran.r-project.org/src/contrib/Archive/party/party_1.0-25.tar.gz",
repos=NULL, type="source")'  
  
#############################################  
# Download and install FSL ICA-FIX  
RUN apt-get -y update && \  
apt-get install -y wget && \  
wget -nv http://www.fmrib.ox.ac.uk/~steve/ftp/fix1.066.tar.gz -O /fix.tar.gz
&& \  
mkdir -p /tmp/fix && \  
cd /tmp/fix && \  
tar zxvf /fix.tar.gz --exclude="compiled/" \--exclude="MCRInstaller.zip" && \  
mv /tmp/fix/fix* /opt/fix && \  
rm /fix.tar.gz && \  
cd / && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV FSL_FIXDIR=/opt/fix  
  
# Download and install Matlab Compiler Runtime v8.5 (2015a)  
# Install the MCR dependencies and some things we'll need and download the MCR  
# from Mathworks -silently install it  
# See http://www.mathworks.com/products/compiler/mcr/ for more info.  
# Adapted from https://github.com/flywheel-apps/matlab-mcr  
RUN apt-get -qq update && apt-get -qq install -y \  
unzip \  
xorg \  
wget \  
curl && \  
mkdir /mcr-install && \  
mkdir /opt/mcr && \  
cd /mcr-install && \  
wget -nv
http://www.mathworks.com/supportfiles/downloads/R2015a/deployment_files/R2015a/installers/glnxa64/MCR_R2015a_glnxa64_installer.zip
&& \  
cd /mcr-install && \  
unzip -q MCR_R2015a_glnxa64_installer.zip && \  
./install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \  
cd / && \  
rm -rf mcr-install  
  
#ENV LD_LIBRARY_PATH
/opt/mcr/v85/runtime/glnxa64:/opt/mcr/v85/bin/glnxa64:/opt/mcr/v85/sys/os/glnxa64
#skip this  
ENV XAPPLRESDIR /opt/mcr/v85/X11/app-defaults  
  
#############################################  
# Download and install FSL 5.0.9  
#Build-time key retrieval is sometimes unable to connect to keyserver.
Instead, download the public key manually and store it in plaintext  
#within repo. You should run these commands occassionally to make sure the
saved public key is up to date:  
#gpg --keyserver hkp://pgp.mit.edu:80 --recv 0xA5D32F012649A5A9 && \  
#gpg --export --armor 0xA5D32F012649A5A9 > neurodebian_pgpkey.txt && \  
#gpg --batch --yes --delete-keys 0xA5D32F012649A5A9  
COPY neurodebian_pgpkey.txt /tmp/  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl && \  
curl -sSL http://neuro.debian.net/lists/trusty.us-ca.full >>
/etc/apt/sources.list.d/neurodebian.sources.list && \  
apt-key add /tmp/neurodebian_pgpkey.txt && \  
apt-get update && \  
apt-get install -y fsl-core=5.0.9-4~nd14.04+1 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure FSL environment  
ENV FSLDIR=/usr/share/fsl/5.0  
ENV FSL_DIR="${FSLDIR}"  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
ENV PATH=/usr/lib/fsl/5.0:$PATH  
ENV FSLMULTIFILEQUIT=TRUE  
ENV POSSUMDIR=/usr/share/fsl/5.0  
ENV LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH  
ENV FSLTCLSH=/usr/bin/tclsh  
ENV FSLWISH=/usr/bin/wish  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
  
#############################################  
# Download and install Connectome Workbench  
RUN apt-get update && apt-get -y install connectome-
workbench=1.2.3-1~nd14.04+1  
  
ENV CARET7DIR=/usr/bin  
  
#############################################  
# Download and install HCP Pipelines  
#latest v3.x = v3.22.0  
#latest v4.x = v4.0.0-alpha.5  
#Need to use this 2017-08-24 commit to fix bugs in v4.0.0-alpha.5:
90b0766636ba83f06c9198206cc7fa90117b0b11  
RUN apt-get -y update && \  
apt-get install -y wget && \  
apt-get install -y --no-install-recommends python-numpy && \  
wget -nv https://github.com/Washington-
University/Pipelines/archive/90b0766636ba83f06c9198206cc7fa90117b0b11.tar.gz
-O pipelines.tar.gz && \  
cd /opt/ && \  
tar zxvf /pipelines.tar.gz && \  
mv /opt/Pipelines-* /opt/HCP-Pipelines && \  
rm /pipelines.tar.gz && \  
cd / && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV HCPPIPEDIR=/opt/HCP-Pipelines  
  
# Manual patche for hcp_fix, re-compiled PostFix and RSS, etc.  
COPY pipeline_patch/ ${HCPPIPEDIR}/  
  
# Manual patch for settings.sh and re-compiled FIX  
COPY fix_patch/ ${FSL_FIXDIR}/  
  
#############################################  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
WORKDIR ${FLYWHEEL}  
  
# Copy executable/manifest to Gear  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Copy additional scripts and scenes  
COPY scripts/*.sh scripts/*.bat ${FLYWHEEL}/scripts/  
  
# ENV preservation for Flywheel Engine  
RUN env -u HOSTNAME -u PWD | \  
awk -F = '{ print "export " $1 "=\"" $2 "\"" }' > ${FLYWHEEL}/docker-env.sh  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  

