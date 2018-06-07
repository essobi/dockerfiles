FROM hroest/openms-lib-2.1  
WORKDIR /openms-build  
  
# make OpenMS all  
RUN make TOPP -j6  
RUN make UTILS -j6  
# this works  
## RUN make -j6  
## RUN make clean  
RUN rm -rf /OpenMS/.git  
RUN rm -rf /OpenMS/src  
  
WORKDIR /  
ENV PATH="/openms-build/bin/:${PATH}"  

