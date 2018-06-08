FROM alpine:latest  
MAINTAINER Maximilian Pachl <m@ximilian.info>  
  
# install all necessary tools  
RUN apk add --update \  
git openssh-client && \  
  
# remove build dependencies  
rm -rf /var/cache/apk/*  
  
# add the user which will run the build  
RUN adduser -D -u 1000 -g 'sackci' sackci  
  
# setup the scm environment  
ADD scm /usr/bin  
RUN chown sackci:sackci /mnt && \  
chmod 755 /usr/bin/scm  
  
# container startup behaviour  
USER sackci  
ENTRYPOINT ["/usr/bin/scm"]  

