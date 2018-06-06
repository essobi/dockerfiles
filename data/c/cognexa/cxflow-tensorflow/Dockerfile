ARG tag="latest"  
FROM cognexa/cxflow:"${tag}"  
MAINTAINER Cognexa Solutions s.r.o. <docker@cognexa.com>  
  
ARG tag  
RUN if [ "${tag}" = "cuda" ]; then \  
pacman --noconfirm --needed -S python-tensorflow-opt-cuda; \  
pacman --noconfirm -Rdd nvidia-utils; \  
pacman --noconfirm -Rns $(pacman -Qtdq); \  
else \  
pacman --noconfirm --needed -S python-tensorflow-opt; \  
fi \  
&& pacman --noconfirm --needed -S tensorboard \  
&& paccache -rfk0  
  
# install cxflow-tensorflow  
RUN pip install --no-cache-dir git+https://github.com/Cognexa/cxflow-
tensorflow.git  

