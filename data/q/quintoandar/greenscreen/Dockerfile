FROM node:8.9.4  
ENV GREENSCREEN_HOME /opt/greenscreen  
  
RUN git clone https://github.com/groupon/greenscreen.git ${GREENSCREEN_HOME}
&& \  
adduser --gecos " " \--disabled-password greenscreen && \  
cd /opt/greenscreen && \  
npm install && \  
rm -rf ${GREENSCREEN_HOME}/.git && \  
apt-get update && \  
apt-get install -y nginx && \  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
apt-get clean  
  
ADD start ${GREENSCREEN_HOME}/start  
  
ADD nginx/greenscreen.conf /etc/nginx/sites-available/default  
  
WORKDIR ${GREENSCREEN_HOME}  
  
EXPOSE 4994 80  
ENTRYPOINT ${GREENSCREEN_HOME}/start  
  

