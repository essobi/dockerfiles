FROM treemo/rfcat  
  
  
# upgrade image  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# install ooktools  
RUN pip install ooktools  
  
# clean / optimise docker size  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/* /var/tmp/*  

