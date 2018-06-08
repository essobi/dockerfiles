FROM tahoelafs/base:1.12.1  
WORKDIR /root  
VOLUME /root/.tahoe  
EXPOSE 3456  
RUN pip install txtorcon tahoe-lafs[i2p] tahoe-lafs[tor]  
  
CMD tahoe run  

