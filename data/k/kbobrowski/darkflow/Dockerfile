FROM kbobrowski/tensorflow-gpu-opencv  
  
LABEL maintainer="kamil.bobrowski@gmail.com"  
  
# pip  
RUN apt-get update && apt-get install -y \  
python-pip  
  
# Cython  
RUN pip install --no-cache-dir Cython  
  
# darkflow  
RUN git clone https://github.com/thtrieu/darkflow.git \  
&& cd darkflow \  
&& pip install .  

