############################################################  
# Dockerfile to build XXXXX tool container image  
# Based on debian Jessie/8  
############################################################  
  
# Set the base image to debian  
FROM debian:latest  
  
MAINTAINER Sébastien Letort sletort@irisa.fr  
  
################## DEPENDENCIES INSTALLATION ######################  
RUN apt-get update \  
&& apt-get -y dist-upgrade  
  
ENV PACKAGES build-essential \  
git ca-certificates \  
jq bc rs curl unzip redland-utils \  
cmake pkg-config automake protobuf-compiler \  
libncurses-dev libbz2-dev libprotoc-dev libjansson-dev libtool \  
librdf-dev bison flex lzma-dev liblzma-dev liblz4-dev  
  
RUN apt-get install -y --no-install-recommends ${PACKAGES}  
Run apt-get clean  
  
ENV DIR /opt  
  
################## VG INSTALLATION ######################  
  
# directory containing source code  
# should be under $DIR  
ENV SOURCE_DIR /opt/src  
  
RUN mkdir -p ${SOURCE_DIR}  
WORKDIR ${SOURCE_DIR}  
  
  
## get code source  
#--- from git repo  
ENV GIT https://github.com/vgteam/vg.git  
ENV TAG v1.6.0  
  
RUN git clone --recursive ${GIT}  
WORKDIR vg  
RUN git checkout ${TAG}  
  
#--- /from git repo  
  
## compile / install  
RUN . ./source_me.sh \  
&& make static  
  
################## Dockerfile usage ######################  
## the command launched by default when running the container  
ENTRYPOINT ["./bin/vg"]  
# CMD ["-help"]  
  
################## METADATA ######################  
MAINTAINER "sletort"  
  
LABEL ANNOT.Name="vg" \  
ANNOT.Version="v1.6" \  
# ANNOT.Licence="" \  
# ANNOT.Description="" \  
ANNOT.author="Sébastien Letort" \  
ANNOT.author_URI="https://www.researchgate.net/profile/Sebastien_Letort" \  
# ANNOT.Homepage="" \  
# ANNOT.Reference="['']" \  
# ANNOT.Vendor="" \  
# ANNOT.Requires="['']" \  
# ANNOT.Provides="['']" \  
# ANNOT.EDAM_Operation="['']" \  
# ANNOT.EDAM_Topic="['']" \  
# ANNOT.Support_URL=""  
  
# Comment to translate edam code in labels (for human comprehension).  
#EDAM_Operation  
# operation_0484 - SNP detection  
#  
#EDAM_Topic  
# topic_2885 - DNA polymorphism  
  

