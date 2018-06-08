FROM nvidia/cuda:8.0-cudnn6-runtime  
MAINTAINER Borodin Gregory <grihabor@mail.ru>  
  
RUN apt update \  
&& apt install -y \  
python3 \  
python3-tk \  
python3-pip  
  
RUN pip3 install --no-cache-dir --upgrade pip  
RUN pip3 install --no-cache-dir numpy  
RUN pip3 install --no-cache-dir scipy  
RUN pip3 install --no-cache-dir scikit-learn  
RUN pip3 install --no-cache-dir scikit-image  
RUN pip3 install --no-cache-dir pandas  
RUN pip3 install --no-cache-dir h5py  
RUN pip3 install --no-cache-dir opencv-python  
RUN pip3 install --no-cache-dir tensorflow-gpu==1.4  
RUN pip3 install --no-cache-dir keras  
  

