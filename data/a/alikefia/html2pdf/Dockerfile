FROM node:8-slim  
  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /src/*.deb  
  
COPY . /app/  
WORKDIR app  
  
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true  
RUN yarn  
  
ENV CHROMIUM_EXEC_PATH /opt/google/chrome-unstable/chrome  
ENV CHROMIUM_NO_SANDBOX 1  
EXPOSE 3000  
CMD ["yarn", "start"]  

