FROM binhex/arch-base:2017102500  
MAINTAINER binhex  
  
# additional files  
##################  
  
# add install bash script  
ADD build/root/*.sh /root/  
  
# install app  
#############  
  
# run bash script to update base image, set locale, install supervisor and
cleanup  
RUN chmod +x /root/*.sh && \  
/bin/bash /root/install.sh  
  
# run bash  
CMD ["/bin/bash"]  

