FROM debian:jessie  
MAINTAINER Carles Amigó, fr3nd@fr3nd.net  
  
RUN apt-get update && apt-get install -y \  
bundler \  
curl \  
git \  
ruby \  
unzip \  
&& rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
ENV BOOTSTRAP_VERSION 4.0.0-alpha  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs build-essential  
RUN npm install -g grunt-cli  
  
WORKDIR /usr/src  
RUN curl -L
https://github.com/twbs/bootstrap/archive/v${BOOTSTRAP_VERSION}.zip >
/tmp/bootstrap.zip && unzip /tmp/bootstrap.zip && rm -f /tmp/bootstrap.zip &&
mv /usr/src/bootstrap-${BOOTSTRAP_VERSION}/ /usr/src/bootstrap/  
WORKDIR /usr/src/bootstrap  
RUN npm install  
RUN bundle  

