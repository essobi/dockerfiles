FROM svendowideit/ambassador  
MAINTAINER feng.zh@gmail.com  
  
ADD expose.sh /tmp/expose.sh  
  
RUN cat /tmp/expose.sh /bin/run.sh > /tmp/run.sh && \  
cp /tmp/run.sh /bin/run.sh && \  
chmod +x /bin/run.sh && \  
rm /tmp/expose.sh /tmp/run.sh  

