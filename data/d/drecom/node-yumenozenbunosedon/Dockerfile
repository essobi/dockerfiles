From node:latest  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y rsync python python-pip build-
essential libssl-dev libffi-dev python-dev xvfb firefox-esr \  
&& apt-get clean \  
&& npm install -g node-gyp \  
&& wget -q https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg -i google-chrome-stable_current_amd64.deb || (apt -f install -y &&
dpkg -i google-chrome-stable_current_amd64.deb) \  
&& rm -f google-chrome-stable_current_amd64.deb \  
&& pip install awscli  

