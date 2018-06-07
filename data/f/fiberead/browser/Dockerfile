FROM ubuntu:18.04  
# ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en'  
ENV LANG='C.UTF-8' \  
USER=deployer  
  
WORKDIR /apps  
COPY Gemfile Gemfile.lock install_webdrivers ./  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https ca-certificates gnupg \  
curl wget unzip zip \  
libnss3-dev zlib1g-dev liblzma-dev \  
build-essential ruby2.5 ruby2.5-dev \  
xvfb imagemagick libmagickwand-dev \  
\--no-install-recommends \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update && apt-get install -y \  
google-chrome-stable firefox --no-install-recommends \  
&& groupadd -r ${USER} && useradd -r -g ${USER} -G audio,video ${USER}
\--shell /bin/bash --create-home \  
&& mkdir /home/${USER}/.webdrivers \  
&& chown -R ${USER}:${USER} /home/${USER} \  
&& chown -R ${USER}:${USER} /apps \  
&& gem install bundle --no-ri --no-rdoc \  
&& bundle install \  
&& rm -rf /var/lib/apt/lists/*  
  
USER ${USER}  
  
RUN ./install_webdrivers  
  
# EXPOSE 9222  
CMD ["ruby", "./main.rb"]  

