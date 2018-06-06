FROM node:8  
  
RUN apt-get update && apt-get install -y libnss3 libxss1 libasound2
libpangocairo-1.0-0 libx11-xcb-dev libxcomposite1 libxcursor1 libxdamage1
libxi6 libxtst6 libcups2 libxrandr-dev libgconf-2-4 libatk1.0-0 libgtk-3-0
libpng-dev  
  
RUN npm init -f && yarn add critical@1.2.2 --no-lockfile && rm -rf
node_modules  
  
RUN npm install --save critical@1.2.2 && rm -rf node_modules package-lock.json
package.json  

