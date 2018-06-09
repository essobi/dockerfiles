### Dockerfile  
#  
# Tokenpass development image  
#  
FROM tokenly/devweb-sass  
  
ARG GITHUB_TOKEN  
ARG GITHUB_BRANCH  
ENV GITHUB_BRANCH ${GITHUB_BRANCH:-development}  
  
# update supervisord conf.d  
ADD ./supervisor/conf.d/* /etc/supervisor/conf.d/  
  
# github token  
USER tokenly  
RUN if [ "$GITHUB_TOKEN" ]; then \  
echo "Configuring composer with your github token"; \  
/usr/local/bin/composer.phar config -g github-oauth.github.com
${GITHUB_TOKEN}; \  
else echo "********* No github token defined. Use --build-arg
GITHUB_TOKEN=xxxxxxx *********"; \  
fi;  
USER root  
  
  
# create an app environment  
USER root  
RUN mkdir -p /app/current /app/current.dist  
RUN chown -R tokenly:tokenly /app/current /app/current.dist  
  
# copy the nginx configuraton for modification  
RUN cp -r /etc/php/7.0/fpm /etc/php/7.0/fpm.dist  
  
# download and deploy the code  
USER tokenly  
RUN git clone https://github.com/tokenly/tokenpass /app/current.dist  
RUN cd /app/current.dist && git pull  
# default to the development branch (by default)  
RUN cd /app/current.dist && git checkout $GITHUB_BRANCH  
RUN cd /app/current.dist && sh .deploy.sh  
USER root  
  
# add the project scripts and install the dependencies  
ADD ./bin /app/bin  
RUN chown -R tokenly:tokenly /app/bin  
USER tokenly  
RUN cd /app/bin && /usr/local/bin/composer.phar install --prefer-dist --no-
progress  
USER root  
  
# share the volumes  
VOLUME /app/current  
VOLUME /etc/php/7.0/fpm  
  

