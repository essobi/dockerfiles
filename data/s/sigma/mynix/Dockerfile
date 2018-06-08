FROM nixos/nix  
MAINTAINER Yann Hodique <yann.hodique@gmail.com>  
  
RUN apk add --update coreutils  
  
VOLUME /target  
ADD run.sh /run.sh  
  
CMD [ "/run.sh" ]  

