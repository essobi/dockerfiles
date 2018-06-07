FROM hroest/openms-lib-2.2  
WORKDIR /openms-build  
  
# make OpenMS all  
RUN make TOPP -j6 && make UTILS -j6  
  
WORKDIR /  
ENV PATH="/openms-build/bin/:${PATH}"  

