FROM bioconductor/devel_core2  
  
ADD etc/fix-attrs.d/00-runscripts /etc/fix-attrs.d/  
  
ADD etc/cont-init.d/userconf /etc/cont-init.d/  
  
ADD tmp/install /tmp/  
  
RUN /tmp/install  

