FROM ubuntu:16.04  
# Install wget  
RUN apt-get update && apt-get install -y git unzip wget cmake build-essential
g++ zlib1g-dev libboost-all-dev  
  
RUN git clone https://github.com/pezmaster31/bamtools && cd bamtools && mkdir
build && cd build && cmake .. && make && cd /  
  
RUN wget http://packages.seqan.de/seqan-library/seqan-library-2.1.1.zip &&
unzip seqan-library-2.1.1.zip && cd /  
  
RUN wget
"http://downloads.sourceforge.net/project/softsv/SoftSV_1.4.2.zip?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fsoftsv%2F&ts=1462296985&use_mirror=ufpr"
-O "SoftSV_1.4.2.zip" && \  
unzip SoftSV_1.4.2.zip && \  
cd SoftSV_1.4.2 && \  
sed 's/\/YourPath\/bamtools/\/bamtools/g' makefile > make_temp && \  
sed 's/\/YourPath\/seqan/\/seqan-library-2.1.1/g' make_temp > make_temp2 && \  
mv makefile makefileOLD && mv make_temp2 makefile && \  
make  
  
env LD_LIBRARY_PATH /bamtools/lib:$LD_LIBRARY_PATH  
env PATH /SoftSV_1.4.2:$PATH  

