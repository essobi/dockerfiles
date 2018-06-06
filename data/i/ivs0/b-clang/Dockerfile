FROM ivs0/b-ros  
  
RUN apt-get update && apt-get install -y git software-properties-common \  
&& add-apt-repository ppa:george-edison55/cmake-3.x && apt-get update \  
&& apt-get install -y zip unzip wget genromfs make clang-3.5 lldb-3.5 cmake \  
python-empy python-argparse build-essential  
  
ENV CC=/usr/bin/clang-3.5 CXX=/usr/bin/clang++-3.5  

