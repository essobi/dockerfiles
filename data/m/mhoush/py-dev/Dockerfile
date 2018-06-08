FROM higebu/tox  
  
RUN apk add --update \  
make && \  
pyenv install 3.3.6 && \  
pyenv global 3.5.0 2.7.10 3.4.3 3.3.6 && \  
pip install --upgrade pip==8.1.2 && \  
rm -rf /var/tmp/* /var/cache/apk/* /tmp/*  
  
RUN echo 'eval "$(pyenv init -)"' >> /root/.profile  
  
ONBUILD COPY . /usr/src/app  
VOLUME /usr/src/app  
WORKDIR /usr/src/app  

