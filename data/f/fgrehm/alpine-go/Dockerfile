FROM golang:1.6.0-alpine  
MAINTAINER Fabio Rehm "fgrehm@gmail.com"  
RUN apk add --update --no-cache bash \  
bash-completion \  
build-base \  
git \  
mercurial  
  
ENV HOME="/home/developer" \  
GOROOT="/usr/local/go" \  
GOBIN="/go/bin" \  
PATH="/home/developer/bin:/go/bin:/usr/local/go/bin:$PATH"  
RUN set -x \  
&& mkdir -p $HOME/bin \  
&& echo 'source /etc/profile.d/bash_completion.sh' >> $HOME/.bashrc \  
&& echo "alias ll='ls -lah'" >> $HOME/.bashrc \  
&& go get github.com/parkghost/watchf/... \  
&& go get github.com/constabulary/gb/... \  
&& rm -rf /tmp/* \  
&& addgroup developer -g 1000 \  
&& adduser -u 1000 -D -s /bin/bash -G developer developer \  
&& chown 1000:1000 -R $HOME \  
&& mkdir -p $GOPATH \  
&& chown 1000:1000 -R $GOPATH \  
&& mkdir -p $GOROOT \  
&& chown 1000:1000 -R $GOROOT  
  
USER developer  
WORKDIR /code  
CMD /bin/bash  

