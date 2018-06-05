# base image (stripped down ubuntu for Docker)  
FROM phusion/baseimage  
  
# metadata  
LABEL base.image="ubuntu"  
LABEL version="1"  
LABEL software="AMRtime"  
LABEL tags="Genomics"  
  
# maintainer  
MAINTAINER Finlay Maguire <finlaymaguire@gmail.com>  
  
# install system dependencies  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test && \  
apt-get update && \  
apt-get install -y g++-5 gcc-5 cmake libgtest-dev xz-utils git && \  
ln -f -s /usr/bin/g++-5 /usr/bin/g++  
  
# install seqan  
ADD http://packages.seqan.de/seqan-library/seqan-library-2.4.0.tar.xz .  
  
RUN tar xvf seqan-library-2.4.0.tar.xz && cp -r seqan-library-2.4.0/include
seqan-library-2.4.0/share /usr/local/  
  
# install gtest  
RUN cd /usr/src/gtest && \  
cmake CMakeLists.txt && \  
make && \  
cp *.a /usr/lib && cd  
  
# install art  
ADD
https://www.niehs.nih.gov/research/resources/assets/docs/artbinmountrainier20160605linux64tgz.tgz
.  
RUN tar xvf artbinmountrainier20160605linux64tgz.tgz && cp
art_bin_MountRainier/art_illumina /usr/bin  
  
# install AMRtime  
RUN git clone https://github.com/beiko-lab/AMRtime && cd AMRtime && \  
cd build && cmake -Dtest=ON .. && make  
  
# test AMRtime  
# RUN ./bin/run_unit_tests  
# move to bin  
RUN cp ./AMRtime/build/bin/amrtime /usr/bin  
  
# move to workdir  
WORKDIR /data/  
  
# set rgi executable as cmd to allow overriding  
# ENTRYPOINT ["amrtime"]  

