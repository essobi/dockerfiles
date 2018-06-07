FROM alpine  
  
MAINTAINER Henrik Jonsson <me@hkjn.me>  
  
RUN apk add --no-cache bash ruby git  
  
COPY ["dirty_repo.sh", "/usr/bin/"]  
COPY ["git-wtf.rb", "/usr/bin/"]  
  
CMD ["dirty_repo.sh"]  

