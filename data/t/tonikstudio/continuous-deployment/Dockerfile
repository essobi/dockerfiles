FROM alpine:3.6  
  
RUN apk add \--no-cache \  
bash \  
openssh-client \  
git \  
rsync  
  
RUN mkdir -p ~/.ssh  
RUN echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config  

