FROM finalduty/archlinux  
  
# add installation script  
ADD install.sh /install.sh  
ADD discover.sh /discover.sh  
  
# install python  
RUN /install.sh py2  
  
CMD /discover.sh && bash  

