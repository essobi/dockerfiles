from alpine  
  
run apk add --no-cache --update ca-certificates && update-ca-certificates  
run apk add --no-cache --update openssl zsh git docker tar curl  
run git clone git://github.com/robbyrussell/oh-my-zsh.git /root/.oh-my-zsh  
  
run apk del git openssl ca-certificates  
  
run curl https://get.docker.com/builds/Linux/x86_64/docker-1.13.1.tgz | tar
xvz  
run mv /docker/docker /bin/docker  
run rm -rf /docker  
  
copy zshrc /root/.zshrc  
  
env SHELL=/bin/zsh  
env HISTFILE=/root/.config/zsh/zsh_history  
  
entrypoint /bin/zsh

