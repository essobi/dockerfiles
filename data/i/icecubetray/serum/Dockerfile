FROM icecubetray/alpine-icy  
MAINTAINER icecubetray  
  
COPY sbin/run.sh /sbin/run_serum_cst  
RUN dos2unix -u /sbin/run_serum_cst  
  
CMD [ "/sbin/run_serum_cst" ]  

