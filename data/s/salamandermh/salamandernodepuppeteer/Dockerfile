FROM node:8.9.4  
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org  
RUN npm install -g pm2  
  
# 修改时区  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
#
安装puppeter依赖：https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md  
RUN apt-get update && apt-get install -y libasound2 libatk1.0-0 libc6
libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4
libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0
libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1
libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1
libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3
lsb-release xdg-utils wget  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
CMD [ "pm2-runtime", "start", "pm2.json" ]

