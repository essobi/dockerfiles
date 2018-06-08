FROM fjukstad/seqbase  
  
USER root  
WORKDIR /tools  
RUN wget https://github.com/COMBINE-
lab/salmon/releases/download/v0.8.2/Salmon-0.8.2_linux_x86_64.tar.gz  
RUN tar -xzf Salmon-0.8.2_linux_x86_64.tar.gz  
RUN mv Salmon-0.8.2_linux_x86_64 salmon  
USER worker  
  
ENTRYPOINT ["salmon/bin/salmon"]  

