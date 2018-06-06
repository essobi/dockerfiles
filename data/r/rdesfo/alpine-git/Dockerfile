  
FROM rdesfo/alpine-bash:latest  
MAINTAINER Ryan Desfosses <ryan@desfo.org>  
  
USER root  
  
RUN apk add --update \  
git \  
git-bash-completion \  
git-perl \  
&& rm -fr /var/cache/apk/*  
  
USER user  
WORKDIR /home/user  
  
RUN mkdir /home/user/app  
  
ENTRYPOINT ["bash"]  

