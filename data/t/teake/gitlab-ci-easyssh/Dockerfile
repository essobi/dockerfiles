FROM alpine:latest  
  
LABEL maintainer="teake.nutma@gmail.com"  
LABEL version="1.0"  
LABEL description="Easily add private SSH keys during your GitLab CI jobs"  
  
RUN apk --no-cache add \  
openssh-client \  
rsync \  
git  
  
RUN mkdir -p ~/.ssh  
RUN echo -e "Host *\n\tStrictHostKeyChecking no" > ~/.ssh/config  
  
COPY ssh-addkey.sh /usr/bin/ssh-addkey  

