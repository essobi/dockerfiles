FROM simsofast/base  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
WORKDIR /tmp  
  
# Install calculix  
COPY install_calculix.sh /tmp  
RUN bash install_calculix.sh \  
&& rm install_calculix.sh  
  
# Install pyt3 toolchain  
COPY install_pyt3.sh /tmp  
RUN bash install_pyt3.sh \  
&& rm install_pyt3.sh  
  
# USAGE:  
# sudo docker run -it --rm simsofast/pyt3 bash -c "source activate pyt3 &&
python <params>"  
WORKDIR /root  

