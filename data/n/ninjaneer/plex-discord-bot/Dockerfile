FROM node  
  
#configure timezone  
ENV TIMEZONE "America/Detroit"  
RUN rm -f /etc/localtime && \  
ln -s "/usr/share/zoneinfo/${TIMEZONE}" /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone  
  
#get dependencies  
RUN apt-get update && apt-get install -y \  
git \  
vim  
  
#getting source code  
RUN mkdir -p /repo && \  
cd /repo/ && \  
git clone https://github.com/danxfisher/Plex-Discord-Bot.git && \  
cd /repo/Plex-Discord-Bot && \  
npm install  
  
COPY ./init.sh /  
RUN chmod +x /init.sh  
  
#start image  
ENTRYPOINT ["/init.sh"]  

