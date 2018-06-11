FROM node:alpine  
  
RUN apk add --update --no-cache \  
wget curl ca-certificates openssl \  
zsh vim \  
git openssh \  
elinks \  
ruby \  
&& echo 'apk ran okay'  
  
# if fails use $ apk add --update ca-certificates openssl && update-ca-
certificates  
RUN zsh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)" ||true  
  
RUN gem install sass || true  
  
RUN yarn global add \  
http-server \  
bower yo \  
firebase-tools \  
polymer-cli vue-cli \  
&& npm i -g --unsafe-perm now \  
&& echo 'yarn global ran okay'  
  
ENV YARN_VERSION 0.27.5  
RUN curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& rm yarn-v$YARN_VERSION.tar.gz  
  
RUN echo 'alias bower="bower --allow-root"' >> ~/.zshrc  
  
# puhl@kali:~$ docker run -it --rm tg-workstation  
# ➜ / git --version  
# git version 2.13.0  
# ➜ / node --version  
# v8.1.2  
# ➜ / npm --version  
# 5.0.3  
# ➜ / yarn --version  
# 0.24.6  
# ➜ / sass --version  
# Sass 3.4.24 (Selective Steve)  
# ➜ / bower --version  
# 1.8.0  
# ➜ / polymer --version  
# 1.2.0  
# ➜ / firebase --version  
# 3.9.1  
# ➜ /app git:(vue) vue --version  
# 2.8.2  
RUN git config --global user.name "luis-puhl" && \  
git config --global user.email "luispuhl@gmail.com" && \  
git config --global core.fileMode false  
  
# (npm) http-server  
EXPOSE 80 8080  
# polymer serve  
EXPOSE 8081  
# ng serve  
EXPOSE 4200  
# firebase login and serve  
EXPOSE 9005 5000  
VOLUME [ "/app" ]  
WORKDIR "/app"  
  
ENTRYPOINT ["zsh"]  

