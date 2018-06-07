FROM mhart/alpine-node  
  
# install app  
COPY ./README.md /data/README.md  
WORKDIR /data  
  
# get git for bower, ruby* to get sass for polymer  
ARG devDeps="git openssh ruby ruby-rdoc ruby-irb"  
ARG gems="sass"  
# add an `app` user and install some sytem deps.  
# we create a new 1000 uid user to call npm install, so we don't have any
restrictions  
# if there is any "install" or "postinstall" rule calling "npm" or "bower" in
a subdir.  
# We link the eventually mounted /data/.ssh and /data/.npmrc files to the
app's home dir.  
RUN addgroup app \  
&& adduser -h /home/app -s /bin/sh -D -G app app \  
&& chown -R app.app /data \  
&& su -l app -c "ln -s /data/.ssh /home/app/.ssh" \  
&& su -l app -c "ln -s /data/.npmrc /home/app/.npmrc" \  
&& echo 'http://alpine.gliderlabs.com/alpine/latest-stable/main' >
/etc/apk/repositories \  
&& apk update && apk add ${devDeps} \--no-cache \  
&& gem install ${gems}  
  
# drop root privileges  
USER app  
  
ENTRYPOINT ["npm", "i"]  

