FROM debian:8.5  
MAINTAINER Chienchi Lo <chienchi@lanl.gov>  
  
LABEL version="1.0"  
LABEL software="targetNGS"  
LABEL description="Pipeline for assay design evaluation."  
LABEL website="https://chienchilo.bitbucket.io/targetedNGS/"  
LABEL tags="genomics"  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git curl make gcc gfortran g++ grep sed  
  
RUN mkdir -p /opt && \  
wget --quiet https://bioedge.lanl.gov/resource/targetngs-35a2b2559149.tgz -O
/opt/targetngs.tgz && \  
cd /opt && tar xvzf targetngs.tgz && cd targetngs && bash INSTALL.sh && \  
echo 'export PATH=/opt/targetngs:/opt/targetngs/ext/miniconda/bin:$PATH' >
/etc/profile.d/targetngs.sh && \  
echo 'export R_LIBS=/opt/targetngs/ext/lib/R_libs' >>
/etc/profile.d/targetngs.sh && \  
apt-get clean  
  
ADD start.sh /start.sh  
  
ENV PATH /opt/targetngs:/opt/targetngs/ext/miniconda/bin:$PATH  
  
ENV R_LIBS /opt/targetngs/ext/lib/R_libs  
  
EXPOSE 3838  
WORKDIR /data/  
  
CMD [ "/start.sh" ]  

