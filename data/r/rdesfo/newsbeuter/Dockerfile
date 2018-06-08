# Run newsbeuter from a container  
#  
# docker run -it \  
# -v newsb_vol:/home/user/.newsbeuter \  
# --name newsb \  
# ryan/newsbeuter  
FROM alpine:latest  
LABEL maintainer "Ryan Desfosses <ryan@desfo.org>"  
  
USER root  
  
RUN apk add --update \  
newsbeuter \  
vim \  
&& rm -fr /var/cache/apk/*  
  
RUN addgroup -g 1000 user \  
&& adduser -D -G user -u 1000 user  
  
ENV HOME /home/user  
ENV TERM xterm-256color  
  
USER user  
WORKDIR $HOME  
  
Entrypoint ["newsbeuter"]  

