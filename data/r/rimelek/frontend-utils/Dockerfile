FROM node:6.9  
SHELL ["bash", "-c"]  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENV RUBY_VERSION=2.3.3  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 \  
&& curl -sSL https://raw.githubusercontent.com/rvm/rvm/stable/binscripts/rvm-
installer | bash -s stable --ruby=$RUBY_VERSION \  
&& source /etc/profile.d/rvm.sh \  
&& gem install compass \  
&& npm install -g gulp bower \  
&& chown node:node /entrypoint.sh \  
&& chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
USER node  
  

