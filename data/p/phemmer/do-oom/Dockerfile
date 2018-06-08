FROM gcc  
  
ENV PATH $PATH:/  
ADD fix.sh /fix  
RUN chmod a+x /fix  
  
ADD do-oom.c /  
RUN gcc do-oom.c -o /do-oom  
  
CMD /do-oom  

