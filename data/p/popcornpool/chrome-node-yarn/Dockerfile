FROM selenium/standalone-chrome  
  
USER root  
  
# Manually install missing shared libs for Chromium.  
RUN apt-get update \  
&& apt-get install git xvfb curl python3 awscli -y \  
&& apt-get install gconf-service libasound2 libatk1.0-0 libc6 libcairo2
libcups2 libdbus-1-3 \  
libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0
libgtk-3-0 libnspr4 \  
libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1
libxcomposite1 \  
libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1
libxss1 libxtst6 \  
ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-
utils -yq  
  
# See https://crbug.com/795759  
RUN apt-get update && apt-get install -yq libgconf-2-4  
  
# Set Chrome binary location to env variable  
ENV CHROME_BIN /usr/bin/google-chrome  
  
# `dumb-init` helps prevent zombie chrome processes.  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
ENTRYPOINT ["dumb-init", "--"]  
  
# Replace shell with bash so we can source files  
RUN sudo rm /bin/sh && sudo ln -s /bin/bash /bin/sh  
  
# node and yarn environment variables  
ENV HOME /home/seluser  
ENV NVM_DIR $HOME/.nvm  
ENV NODE_VERSION 8.11.2  
ENV YARN_VERSION 1.6.0  
# Set home permissions for seluser  
RUN mkdir -p $HOME && chown -R seluser:seluser $HOME  
  
# Switch user to non-privileged.  
USER seluser  
  
# Install nvm (https://github.com/creationix/nvm#install-script)  
RUN mkdir -p $NVM_DIR \  
&& curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash  
RUN source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
# Add node and npm to PATH  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# Install yarn (https://yarnpkg.com/en/docs/install#alternatives-tab)  
RUN curl --silent -o- -L https://yarnpkg.com/install.sh | bash -s -- --version
$YARN_VERSION  
ENV PATH ~/.yarn/bin:~/.config/yarn/global/node_modules/.bin:$PATH  
  
# Confirm installation  
RUN $CHROME_BIN \--version  
RUN node --version  
RUN npm --version  
RUN yarn --version  
RUN aws --version  
  
# Set working directory to home  
WORKDIR $HOME  
  
CMD ["bash"]

