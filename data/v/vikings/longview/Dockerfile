FROM node:4.8  
  
RUN apt-get update && \  
apt-get install -y traceroute net-tools  
  
RUN wget -O /Longview.tar.gz
"https://www.dropbox.com/s/6061y0x96w6cw6r/Longview.tar.gz?dl=0" && \  
tar -zxvf /Longview.tar.gz && \  
cd /bundle/programs/server && \  
npm install  
  
COPY fire.sh /fire.sh  
ENV PORT=80  
  
WORKDIR /bundle  
  
CMD ["/fire.sh"]

