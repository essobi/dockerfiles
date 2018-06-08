FROM alpine:edge  
MAINTAINER Marcel Maatkamp <m.maatkamp@gmail.com>  
  
RUN apk add --update bash wget zip libevent subversion git && \  
rm /var/cache/apk/* && \  
mkdir /projects  
  
WORKDIR /projects  
  
CMD ["bash"]  

