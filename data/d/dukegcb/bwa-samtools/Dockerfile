# Adapted from https://github.com/common-workflow-
language/workflows/blob/master/tools/samtools-Dockerfile  
FROM dukegcb/bwa:0.7.12  
MAINTAINER Dan Leehr "dan.leehr@duke.edu"  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /tmp  
  
### Install required packages (samtools)  
RUN apt-get clean all &&\  
apt-get update &&\  
apt-get install -y \  
libncurses5-dev \  
git && \  
apt-get clean && \  
apt-get purge && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*  
  
### Installing samtools/htslib/tabix/bgzip  
ENV VERSIONH 1.2.1-254-6462e34  
ENV NAMEH htslib  
ENV SHA1H "6462e349d16e83db8647272e4b98d2a92992071f"  
ENV VERSION 1.2-242-4d56437  
ENV NAME "samtools"  
ENV SHA1 "4d56437320ad370eb0b48c204ccec7c73f653393"  
RUN git clone https://github.com/samtools/htslib.git && \  
cd ${NAMEH} && \  
git reset --hard ${SHA1H} && \  
make -j 4 && \  
cd .. && \  
cp ./${NAMEH}/tabix /usr/local/bin/ && \  
cp ./${NAMEH}/bgzip /usr/local/bin/ && \  
cp ./${NAMEH}/htsfile /usr/local/bin/ && \  
strip /usr/local/bin/tabix; true && \  
strip /usr/local/bin/bgzip; true && \  
strip /usr/local/bin/htsfile; true && \  
  
git clone https://github.com/samtools/samtools.git && \  
cd ${NAME} && \  
git reset --hard ${SHA1} && \  
make -j 4 && \  
cp ./${NAME} /usr/local/bin/ && \  
cd .. && \  
strip /usr/local/bin/${NAME}; true && \  
rm -rf ./${NAMEH}/ && \  
rm -rf ./${NAME}/ && \  
rm -rf ./${NAMEH}  
  
  
# Now add the wrapper script  
ADD bwamem-to-samtools.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/bwamem-to-samtools.sh  

