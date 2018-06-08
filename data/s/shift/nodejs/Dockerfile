FROM alpine:3.4  
  
RUN apk add \--update nodejs ruby ruby-rdoc ruby-irb ca-certificates netcat-
openbsd git openssh bash perl python build-base curl docker \  
&& curl -Ls
"https://github.com/dustinblackman/phantomized/releases/download/2.1.1/dockerized-
phantomjs.tar.gz" | tar xz -C / \  
&& npm install -g grunt-cli gulp-cli \  
&& gem install web_translate_it \  
&& apk upgrade \  
&& apk del --purge tar xz && rm -Rf /var/cache/apk/*  

