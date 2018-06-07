FROM launcher.gcr.io/google/nodejs  
MAINTAINER Extreme Solution <devops@extremesolution.com>  
ENV NODE_VER v8.11.1  
RUN install_node $NODE_VER  
RUN apt-get update && apt-get -y install git wget curl  
#RUN git clone https://github.com/prerender/prerender.git /app  
COPY . /app/  
  
ENV PORT 80  
EXPOSE 80  
# Install dumb-init to rape any Chrome zombies  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb  
RUN dpkg -i dumb-init_*.deb  
  
# Install Chromium.  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update && \  
apt-get install -y google-chrome-stable && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN google-chrome-stable --no-sandbox --version > /opt/chromeVersion  
  
WORKDIR /app  
RUN npm --unsafe-perm install  
RUN npm install prerender-memory-cache --save  
RUN npm install pm2 -g  
  
#ADD index.html /usr/src/app/  
CMD [ "npm", "run", "prod" ]  

