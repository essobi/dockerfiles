FROM phizaz/tensorflow:gpu  
  
########################################  
# ROOT MODE  
########################################  
USER root  
  
###### install keras #########################  
RUN pip install keras  
  
########################################  
# USER MODE  
########################################  
USER docker  
  
WORKDIR /notebooks  
ENV WORKDIR=/notebooks  
CMD ["jupyter", "notebook", "--ip=*"]  

