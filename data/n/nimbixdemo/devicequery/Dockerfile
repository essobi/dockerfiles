FROM nvidia/cuda:7.5-runtime-ubuntu14.04  
ADD /helloWorld /usr/bin/  
RUN apt-get update && apt-get -y --force-yes install cuda-samples-7.5 && apt-
get clean  
RUN make -C /usr/local/cuda/samples/1_Utilities/deviceQuery  
RUN ln -s /usr/local/cuda/samples/1_Utilities/deviceQuery/deviceQuery /usr/bin  
  
ADD ./NAE/help.html /etc/NAE/help.html  

