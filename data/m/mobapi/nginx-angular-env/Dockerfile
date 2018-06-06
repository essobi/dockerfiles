FROM nginx:1.12  
RUN apt-get update && \  
apt-get install -y curl gnupg2 && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
npm install -g gulp  
  
RUN mkdir /scripts  
  
ADD scripts/* /scripts/  
  
RUN chmod 755 /scripts/startup.sh  
  
RUN cd scripts && npm up  
  
CMD ["sh", "-c", "/scripts/startup.sh"]  

