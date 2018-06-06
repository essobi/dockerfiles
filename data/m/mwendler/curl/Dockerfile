# toy with curl a little  
#  
# docker run --rm mwendler/curl https://letsencrypt.org/  
FROM alpine  
  
MAINTAINER Mike  
  
# install curl  
RUN apk --update add curl \  
\  
# clean up cached artefacts  
&& rm -rf /var/cache/apk/*  
  
# output curl's version by default  
ENTRYPOINT ["curl"]  
CMD ["-V"]  

