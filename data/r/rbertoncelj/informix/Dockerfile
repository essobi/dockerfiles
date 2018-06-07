FROM ibmcom/informix-developer-database  
RUN sed -i 's/ROOTSIZE 300000/ROOTSIZE 10000000/g'
/opt/IBM/informix/etc/onconfig.dev && sed -i 's/ROOTSIZE 300000/ROOTSIZE
10000000/g' /opt/IBM/informix/etc/onconfig.std  

