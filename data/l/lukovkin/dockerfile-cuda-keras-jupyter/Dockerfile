FROM lukovkin/dockerfile-cuda-keras:p3.4  
RUN source activate keras \  
&& conda install -y \  
jupyter \  
matplotlib \  
seaborn  
  
VOLUME /notebook  
WORKDIR /notebook  
EXPOSE 8888  

