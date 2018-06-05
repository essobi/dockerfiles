FROM ubuntu  
  
COPY ./start.js /start.js  
COPY ./run.sh /run.sh  
  
RUN apt-get update && apt-get install -y nsca-client nodejs npm && npm install
--prefix . portscanner && chmod +x /run.sh && chown root:root /run.sh  
  
CMD ["/run.sh"]  

