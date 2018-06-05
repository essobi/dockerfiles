FROM node:8  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG TZ="Europe/Paris"  
ENV TZ $TZ  
RUN \  
apt-get update && \  
apt-get install -qqy apt-transport-https locales && \  
echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && \  
locale-gen && \  
dpkg-reconfigure locales && \  
echo $TZ > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
apt-get autoremove --purge -y && \  
rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
ENV LANGUAGE en_US:en  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
  
RUN \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN \  
apt-get update && \  
apt-get install yarn -yqq && \  
apt-get autoremove --purge -y && \  
rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
CMD ["yarn"]  

