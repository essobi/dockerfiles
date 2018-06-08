## Core installation of R on alpine  
FROM alpine:latest  
  
LABEL maintainer="Joris Meys <jorismeys@gmail.com>"  
  
## edge repositories needed for latest version of R  
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories \  
&& echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
etc/apk/repositories \  
&& apk add \--upgrade --no-cache apk-tools@edge  
  
RUN ["apk", "add", "R@edge"]  
  
CMD ["R"]  

