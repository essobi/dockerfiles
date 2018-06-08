FROM pulsarchem/gcc_5_4  
MAINTAINER Pulsar-Chem  
RUN git clone \--recursive https://github.com/pulsar-chem/Pulsar-Core
/tmp/Pulsar-Core  
RUN ls /tmp/Pulsar-Core/  
WORKDIR /tmp/Pulsar-Core  
RUN ls  
RUN cmake -Bbuild -H. -DCMAKE_C_COMPILER=gcc \  
-DCMAKE_CXX_COMPILER=g++ \  
-DPYTHON_EXECUTABLE=/usr/bin/python3 \   
-DPYTHON_LIBRARIES=/usr/lib/python3.5 \  
-DPYTHON_INCLUDE_DIRS=/usr/include/python3.5  
WORKDIR /tmp/Pulsar-Core/build  
RUN make  
RUN ctest  
RUN make install  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ENV PYTHONPATH /usr/local/modules  

