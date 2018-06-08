FROM nginx:1.9.6  
# NodeJS, Git, bzip2  
RUN apt-get update && \  
apt-get -y install curl && \  
curl -sL https://deb.nodesource.com/setup_0.12 | bash - && \  
apt-get -y install nodejs git bzip2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Gulp, bower  
RUN npm update npm -g  
RUN npm install -g gulp bower  
  
# Source  
ADD app /app  
ADD bower.json /bower.json  
Add .bowerrc /.bowerrc  
ADD gulpfile.js /gulpfile.js  
ADD package.json /package.json  
ADD tasks /tasks  
  
# Dependencies  
RUN bower install --allow-root --config.interactive=false -s  
RUN npm install  
  
# Create dist  
RUN gulp  
  
# Copy to nginx root  
RUN cp -a dist/* /usr/share/nginx/html

