FROM ytnobody/alpine-perl  
MAINTAINER ytnobody <ytnobody@gmail.com>  
  
RUN apk update && apk add openssl-dev jpeg-dev libpng-dev  
  
ADD cpanfile cpanfile  
RUN cpanm -n --installdeps .  
  
ADD app.psgi app.psgi  
  
EXPOSE 7091  
ENTRYPOINT plackup -p 7091  

