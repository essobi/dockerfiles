FROM openms/library  
  
WORKDIR /openms-build  
  
RUN make TOPP && make UTILS && rm -rf src doc CMakeFiles  
  
WORKDIR /  
ENV PATH="/openms-build/bin/:${PATH}"  

