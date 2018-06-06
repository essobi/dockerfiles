FROM node:8-slim  
  
# Install latest chrome browser  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt update -qq && apt-get install -y --no-install-recommends \  
google-chrome-unstable \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone \--depth=1 https://github.com/val92130/openaio-api.git \  
&& cd openaio-api/ \  
&& yarn \  
&& npm install -g pm2  
  
WORKDIR openaio-api  
  
EXPOSE 8081  
CMD ["pm2-docker", "process.yml"]  

