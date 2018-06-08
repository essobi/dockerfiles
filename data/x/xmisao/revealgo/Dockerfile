# xmisao/revealgo  
FROM golang:1.6.3-alpine  
MAINTAINER xmisao  
  
RUN \  
apk add --no-cache git openssh-client && \  
mkdir /revealgo && \  
# faild to clone submodule at the 1st time  
go get github.com/yusukebe/revealgo/cmd/revealgo ; \  
# succeed at the 2nd time  
go get github.com/yusukebe/revealgo/cmd/revealgo  
  
WORKDIR /revealgo  
ENTRYPOINT ["revealgo"]  

