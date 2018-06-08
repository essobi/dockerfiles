FROM node:8-stretch  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list' && \  
apt-get update && apt-get install -y google-chrome-unstable python-pip && \  
pip install awscli && \  
adduser --disabled-password --gecos "" chrome  
  
RUN yarn global add lighthouse@2.9.4  
  
RUN sed -i 's/^.*--disable-setuid-sandbox.*$//'
/usr/local/share/.config/yarn/global/node_modules/lighthouse/chrome-
launcher/chrome-launcher.js  
  
USER chrome  
WORKDIR /home/chrome  
RUN mkdir /home/chrome/.aws  
  
COPY entrypoint.sh .  
  
CMD ["/home/chrome/entrypoint.sh"]  

