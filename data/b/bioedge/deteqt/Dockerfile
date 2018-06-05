FROM debian:8.5  
MAINTAINER Chienchi Lo <chienchi@lanl.gov>  
  
LABEL version="1.0"  
LABEL software="DETEQT"  
LABEL description="Pipeline for assay design evaluation."  
LABEL website="https://github.com/LANL-Bioinformatics/DETEQT"  
LABEL tags="genomics"  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git curl make gcc gfortran g++ grep sed  
  
RUN mkdir -p /opt && \  
cd /opt && git clone https://github.com/LANL-Bioinformatics/DETEQT.git && \  
cd DETEQT && bash INSTALL.sh && \  
echo 'export PATH=/opt/DETEQT:/opt/DETEQT/ext/miniconda/bin:$PATH' >
/etc/profile.d/DETEQT.sh && \  
echo 'export R_LIBS=/opt/targetngs/ext/lib/R_libs' >> /etc/profile.d/DETEQT.sh
&& \  
apt-get clean  
  
ADD start.sh /start.sh  
  
ENV PATH /opt/DETEQT:/opt/DETEQT/ext/miniconda/bin:$PATH  
  
ENV R_LIBS /opt/DETEQT/ext/lib/R_libs  
  
EXPOSE 3838  
WORKDIR /data/  
  
CMD [ "/start.sh" ]  

