FROM node:6.5.0  
  
EXPOSE 8080  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y \  
build-essential \  
curl \  
sudo \  
wget  
  
ENV APP_HOME=/usr/local/nonroot  
ENV APP_LOG=/var/log/app/app.log  
ENV APP_ERR=/var/log/app/app.err  
  
# Create a nonroot user and add it as a sudo user  
RUN /usr/sbin/useradd --create-home --home-dir $APP_HOME \--shell /bin/bash
nonroot  
RUN /usr/sbin/adduser nonroot sudo  
RUN echo "nonroot ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
# Install global node packages  
RUN npm install -g \  
bower \  
nodemon \  
gulp-cli \  
bower-npm-resolver \  
pm2  
  
# Change permissions for folders  
RUN mkdir -p /var/log/app && chmod a+w /var/log/app  
  
# Set working directory and switch user  
WORKDIR $APP_HOME/app  
USER nonroot  
  
# Install npm and bower dependencies  
COPY package.json bower.json .bowerrc ./  
RUN sudo chown -R nonroot .  
RUN npm install && bower install  
  
# Copy source over  
COPY ./ .  
RUN sudo chown -R nonroot .  
  
# Compile front-end files and run app  
RUN gulp sass && gulp compress  
CMD npm start

