# Build  
#  
# git clone https://github.com/lferry007/LargeVis.git .  
# docker build -t largevis .  
#  
#  
# Run  
#  
# docker run -u $UID -v $PWD:/data largevis LargeVis -fea 0 --threads $(nproc)
-input /code/Examples/CondMat/CondMat_network.txt -output
/data/CondMat_vec2D.txt  
#  
#  
FROM python:2.7  
RUN apt-get update && apt-get install -y libgsl0-dev  
  
ADD . /code  
WORKDIR /code  
  
RUN cd Linux && g++ LargeVis.cpp main.cpp -o LargeVis -lm -pthread -lgsl
-lgslcblas -Ofast -march=native -ffast-math && \  
python setup.py install && cp LargeVis /usr/bin && mkdir /data  
  
WORKDIR /data  
  
CMD ["LargeVis", "--help"]  
  

