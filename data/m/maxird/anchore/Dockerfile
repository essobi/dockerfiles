FROM maxird/centos:7  
RUN mkdir -p /storage && \  
cd /storage && \  
mkdir -p conf data feeds user-scripts && \  
ln -sf /storage /root/.anchore && \  
echo 'initialized volume structure'  
  
VOLUME /storage/conf  
VOLUME /storage/data  
VOLUME /storage/feeds  
VOLUME /storage/user-scripts  
  
RUN pip install --upgrade anchore && \  
echo 'Ready to start' > /var/log/anchore.log && \  
echo 'done'  
  
CMD ["tail", "-F", "/var/log/anchore.log"]  

