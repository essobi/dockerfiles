FROM alpine  
  
COPY ./archive /  
  
RUN chmod 755 /archive && \  
ln -s /archive /etc/periodic/15min && \  
ln -s /archive /etc/periodic/daily && \  
ln -s /archive /etc/periodic/hourly && \  
ln -s /archive /etc/periodic/monthly && \  
ln -s /archive /etc/periodic/weekly && \  
mkdir -p \  
/input/15min \  
/input/daily \  
/input/hourly \  
/input/monthly \  
/input/weekly \  
/output/15min \  
/output/daily \  
/output/hourly \  
/output/monthly \  
/output/weekly  
  
CMD crond -f  

