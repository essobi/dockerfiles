FROM hhvm/hhvm:3.21-lts-latest  
  
MAINTAINER Alex Price  
ENV DEBIAN_FRONTEND noninteractive  
  
# Remove sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install packages  
RUN apt-get update  
RUN apt-get -y install \  
git \  
curl \  
libxml2-dev \  
build-essential \  
libssl-dev \  
pkg-config \  
openssh-client \  
apt-transport-https \  
python  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get -y install yarn --no-install-recommends  
  
# Clean apt  
RUN apt-get clean  
  
# SSH-agent  
RUN mkdir -p ~/.ssh  
RUN [[ -f /.dockerenv ]] && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" >
~/.ssh/config  
  
# Install node  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash &&
\  
export NVM_DIR="/root/.nvm" && \  
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \  
nvm install 8.9 lts  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer creates=/usr/local/bin/composer  
RUN php /usr/local/bin/composer global require "fxp/composer-asset-
plugin:~1.1.1" "hirak/prestissimo:^0.3"  
  
# Install google cloud sdk  
RUN curl -fsSL
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-189.0.0-linux-x86_64.tar.gz -o /google-cloud-sdk.tar.gz  
RUN tar -xf /google-cloud-sdk.tar.gz -C /  
RUN /google-cloud-sdk/install.sh --usage-reporting false \--additional-
components kubectl --path-update true  
RUN rm /google-cloud-sdk.tar.gz  
RUN ln -s /google-cloud-sdk/bin/gcloud /usr/bin/  
RUN ln -s /google-cloud-sdk/bin/kubectl /usr/bin/  

