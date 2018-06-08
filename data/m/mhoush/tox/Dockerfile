FROM higebu/tox  
  
RUN pyenv update  
  
RUN apk add --update make && \  
pyenv install 3.3.6 && \  
pyenv install 3.6.1 && \  
pyenv install 3.5.3 && \  
pyenv global 3.5.3 2.7.10 3.4.3 3.3.6 3.6.1 && \  
pip install --upgrade pip && \  
rm -rf /var/tmp/* /var/cache/apk/* /tmp/* /root/.cache/*  
  
ONBUILD COPY . /usr/src/app  
  
VOLUME /usr/src/app  
WORKDIR /usr/src/app  

