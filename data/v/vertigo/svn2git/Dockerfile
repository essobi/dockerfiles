FROM alpine:3.3  
MAINTAINER Raphael Bottino <raphabot@gmail.com>  
  
ENV PACKAGES ruby git git-svn git-perl  
  
# Update and install all of the required packages.  
# At the end, remove the apk cache  
# Install the gem  
RUN apk update && \  
apk upgrade && \  
apk add $PACKAGES && \  
rm -rf /var/cache/apk/* && \  
gem install svn2git --no-ri --no-rdoc  
  
WORKDIR /svn2git  
  
ENTRYPOINT ["svn2git"]  

