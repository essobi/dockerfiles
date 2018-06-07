FROM carlosfrias/centosjava  
MAINTAINER Carlos Frias carlos.frias.01@gmail.com  
  
RUN curl -s get.gvmtool.net | bash  
RUN sed -i 's/gvm_auto_answer=false/gvm_auto_answer=true/g'
/root/.gvm/etc/config  
  
# Add GVM to default profile script  
RUN echo '' >> /root/.bashrc  
RUN echo '[[ -s "/Users/carlosfrias/.gvm/bin/gvm-init.sh" ]] && source
"/Users/carlosfrias/.gvm/bin/gvm-init.sh"' >> /root/.bashrc  
RUN echo '' >> /root/.bashrc  
  
RUN bash -l -c 'gvm i groovy'  
  
CMD ["/bin/bash"]  

