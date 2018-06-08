FROM ubuntu:14.04  
MAINTAINER aalonsog@dit.upm.es  
  
WORKDIR /opt  
  
# Install Ubuntu dependencies  
RUN sudo apt-get update && \  
sudo apt-get install yasm gcc g++ pkg-config make cmake git libgomp1
libglib2.0-dev libboost-regex-dev libboost-thread-dev libboost-system-dev
libboost-test-dev libssl-dev liblzma-dev libbz2-dev liblog4cxx10-dev -y  
  
# Install ffmpeg  
RUN git clone https://github.com/magonzalezc/LHE.git && \  
cd LHE && \  
git checkout -b lhe_develop origin/lhe_develop && \  
./configure --extra-cflags=-fopenmp --extra-ldflags=-fopenmp && \  
sudo make && \  
sudo make install  
  
# Install the project  
RUN git clone https://github.com/ging/payloader.git && \  
cd payloader && \  
cmake . && \  
make  
  
WORKDIR /opt/payloader  
CMD ./prototype1 media/${INPUT_FILE} media/${OUTPUT_FILE}  

