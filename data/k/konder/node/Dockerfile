FROM centos  
  
RUN yum update -y  
RUN yum install -y tar curl wget git gcc gcc-c++ make rubygems  
  
ENV NODE_VERSION 5.11.0  
ENV NPM_VERSION 3.8.6  
RUN wget "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm install -g grunt-cli \  
&& npm install -g bower \  
&& npm cache clear  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.0.1/dockerize-linux-
amd64-v0.0.1.tar.gz  
RUN tar -C /usr/local/bin -xvzf dockerize-linux-amd64-v0.0.1.tar.gz  
  
RUN gem install sass  
  
RUN echo 'LANG="en_US.UTF-8"' > /etc/sysconfig/i18n  
RUN echo 'LC_ALL="en_US.UTF-8"' >> /etc/sysconfig/i18n  
RUN source /etc/sysconfig/i18n  

