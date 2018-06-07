ARG TAG="latest"  
FROM lambdalisue/vim-ci:${TAG}  
MAINTAINER lambdalisue <lambdalisue@hashnote.net>  
  
RUN apk add \--no-cache --virtual build-deps git \  
&& git clone --depth 1 \--single-branch https://github.com/thinca/vim-themis
/opt/github.com/thinca/vim-themis \  
&& git clone --depth 1 \--single-branch https://github.com/vim-jp/vital.vim
/opt/github.com/vim-jp/vital.vim \  
&& apk del build-deps  
  
ENV THEMIS_HOME=/opt/github.com/thinca/vim-themis \  
THEMIS_VIM=/usr/local/bin/vim  
  
ENTRYPOINT ["/opt/github.com/thinca/vim-themis/bin/themis"]  
CMD ["--runtimepath", "/opt/github.com/vim-jp/vital.vim"]  

