FROM alpine:3.7  
LABEL maintainer="rickshinners@gmail.com"  
  
RUN apk update && \  
apk add \  
bash \  
vim \  
htop \  
&& rm -rf /var/cache/apk/*  
  
CMD ["/bin/bash"]

