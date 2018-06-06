FROM switchback/git-debian  
  
# add script to run  
ADD *.sh /usr/local/bin/  
  
RUN ls /usr/local/bin  
  
WORKDIR /var/workspace  
  
CMD /bin/bash /usr/local/bin/setup.sh && \  
/bin/bash /usr/local/bin/checkout.sh $BRANCH  

