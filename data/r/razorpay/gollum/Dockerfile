FROM ruby:alpine  
  
RUN apk --no-cache --update add \  
icu-dev alpine-sdk dumb-init openssh-client \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p /app  
  
COPY ["Gemfile.lock", "Gemfile", "config.ru", "/app/"]  
  
RUN wget -O /tmp/oauth2_proxy.tar.gz
https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-
amd64.go1.8.1.tar.gz && \  
cd /tmp/ && \  
tar -xzf /tmp/oauth2_proxy.tar.gz oauth2_proxy-2.2.0.linux-
amd64.go1.8.1/oauth2_proxy --strip-components=1 && \  
mv /tmp/oauth2_proxy /usr/local/bin/oauth2_proxy && \  
chmod +x /usr/local/bin/oauth2_proxy && \  
rm /tmp/oauth2_proxy.tar.gz  
  
WORKDIR /app  
RUN gem install bundler && bundle install  
  
COPY gollum.sh /  
  
# Disable host key verification and create .ssh directory  
RUN echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \  
mkdir /root/.ssh  
  
ENTRYPOINT ["/gollum.sh"]  
  
COPY ["cron", "/app/"]  
EXPOSE 8080  

