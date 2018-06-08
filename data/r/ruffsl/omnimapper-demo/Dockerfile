FROM cogrob/omnimapper:gtsam  
  
WORKDIR /root  
  
# clone omnimapper project  
RUN git clone https://github.com/CognitiveRobotics/omnimapper.git  
  
# build omnimapper project  
RUN cd omnimapper/ \  
&& mkdir build \  
&& cd build \  
&& cmake .. \  
&& make -j$(nproc)  
  
# build omnimapper ros wrapper  
ADD build.sh omnimapper/build.sh  
RUN ./omnimapper/build.sh  

