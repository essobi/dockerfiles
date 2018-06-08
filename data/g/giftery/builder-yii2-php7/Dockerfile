FROM giftery/supervisord-nginx-php-fpm71  
  
RUN yum install -y git  
  
ENV USER_HOME /home/user  
  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
  
# Builder is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN groupadd -g ${gid} ${group} && useradd -d "$USER_HOME" -u ${uid} -g ${gid}
-m -s /bin/bash ${user}  
  
COPY ./ssh-keys/ /${USER_HOME}/.ssh/  
RUN ssh-keyscan -t rsa bitbucket.org >> $USER_HOME/.ssh/known_hosts && chown
-R ${user}:${group} $USER_HOME && chmod 600 -R $USER_HOME/.ssh/ && chmod 700
$USER_HOME/.ssh/  
  
USER ${user}  
RUN composer config \--global github-oauth.github.com
61e166a9f046dbd59ed5973fd5a4058125de4ab9  
RUN composer global require --no-progress --no-plugins "fxp/composer-asset-
plugin"  
  
WORKDIR /app  
  
CMD ["install"]  
ENTRYPOINT ["composer"]  

