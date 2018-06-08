# Puppeteer v1.4 with ava & slack  
FROM pottava/puppeteer:1.4  
ENV AVA_VERESION=0.25.0 \  
SLACK_SDK_VERSION=4.2.0 \  
SLACK_WEBHOOK_URL=url  
  
# Install libraries  
RUN sudo npm install --global "ava@${AVA_VERESION}" \  
&& sudo npm install --global "@slack/client@${SLACK_SDK_VERSION}"  
  
ADD index.js /home/puppeteer/index.js  
CMD ["ava", "/home/puppeteer/index.js"]  

