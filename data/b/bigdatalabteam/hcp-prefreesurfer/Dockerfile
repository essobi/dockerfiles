# CentOS with FSL.  
# Build via: docker build -f ./Dockerfile.centos5 -t centos5 .  
FROM centos:centos5.11  
MAINTAINER laletscaria@yahoo.co.in  
  
# Update the image with the latest packages  
# Note: the versions of these packages may change over time.  
# Different builds of the container may contain different versions.  
############  
# Packages #  
###########  
# bc- calculator for fslreorient2std  
# curl-devel - cURL is a software package which consists of command line tool
and a library for transferring data using URL syntax  
# epel-release to help pip installation  
# expat-devel - xml parser library  
# fontconfig - Fontconfig package contains a library and support programs used
for configuring and customizing font access  
# freetype contains a library which allows applications to properly render
TrueType fonts  
# gettext helps in producing multi-lingual messages  
# git library for cloining pipelines repository.  
# libpng - libpng is the official PNG reference library  
# libSM - is a library of generally useful C abstractions  
# libstdc++ - a powerful set of reuseable tools in the form of the C++
Standard Library  
# libXrender - used when compiling programs that use freetype fonts  
# libXext - Xorg libraries provide library routines that are used within all X
Window applications  
# openssl-devel - for secure communication  
# perl-ExtUtils-MakeMaker - designed to write a Makefile for an extension
module from a Makefile.PL  
# tar,unzip - to extract .tar.gz and .zip files  
# wget to get files or status from URL's  
# zlib-devel - to support FMRIB file IO  
# numpy - to support FMRIB pipeline execution  
# Adjust yum repositories since CentOS5 now reached EOL  
ADD ./yum.repos/libselinux.repo /etc/yum.repos.d  
ADD ./yum.repos/CentOS-Base.repo /etc/yum.repos.d  
  
RUN yum update -y && yum install -y \  
bc \  
curl-devel \  
epel-release \  
expat-devel \  
fontconfig.x86_64 \  
freetype.x86_64 \  
gettext-devel \  
git \  
libpng.x86_64 \  
libSM.x86_64 \  
libstdc++.x86_64 \  
libXrender.x86_64 \  
libXext.x86_64 \  
openssl-devel \  
perl-ExtUtils-MakeMaker \  
tar \  
unzip \  
wget \  
zlib-devel  
  
RUN rpm --rebuilddb ; \  
yum clean all && yum install -y \  
numpy.x86_64  
  
# Permit access to fsl installation script (must exist locally)  
ADD ./myFslInstallerScript.sh /myFslInstallerScript.sh  
  
# Install fsl to default dir  
RUN echo -e "/usr/local/src" | ./myFslInstallerScript.sh 5.0.6 CentOS5
/usr/local/src /usr/local/etc/  
  
#Clone HCP pipelines  
# Fix the version of pipelines  
RUN wget https://github.com/Washington-
University/Pipelines/archive/v3.19.0.tar.gz -O pipelines.tar.gz; \  
tar zxvf /pipelines.tar.gz -C /usr/local/src/; \  
mv /usr/local/src/Pipelines-* /usr/local/src/pipelines; \  
rm -rf pipelines.tar.gz; \  
mkdir -p /usr/local/src/tools; \  
wget https://ftp.humanconnectome.org/workbench/workbench-rh_linux64-v1.2.3.zip
-O workbench.zip; \  
unzip workbench.zip -d /usr/local/src/tools; \  
rm -rf workbench.zip;  
  
# Set environment variables (run export not needed)  
ENV FSLDIR=/usr/local/src/fsl \  
FSLOUTPUTTYPE=NIFTI_GZ \  
FSLGECUDAQ=cuda.q \  
CARET7DIR=/usr/local/src/tools/workbench/  
  
ENV PATH=${FSLDIR}/bin:${PATH} \  
FSLTCLSH=${FSLDIR}/bin/fsltclsh \  
FSLWISH=${FSLDIR}/bin/fslwish  
  
# Post-installation tweaks for HCP pipelines (undocumented)  
ENV HOME=/usr/local/src \  
PATH=${PATH}:/usr/local/src/pipelines/Examples/Scripts  
  
# Link pipelines folder  
RUN mkdir /usr/local/src/projects; \  
ln -s /usr/local/src/pipelines /usr/local/src/projects/Pipelines;  
  
# Add monitoring script  
ADD ./monitor.sh /bin  
  
# Add execution directory creation script  
ADD ./create-execution-dir.sh /bin  
  
#Add script to generate checksums  
ADD ./checksums.sh /bin  
  
#Add command line arguments script  
ADD ./command-line-script.sh /bin  
  

