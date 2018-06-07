FROM alpine:latest  
  
#install git and openssh-client for getting repo. install bash cuz that's what
we script in  
RUN apk add --update \  
bash \  
git \  
openssh-client \  
&& rm -rf /var/cache/apk/*  
  
ENV BRANCH 'master'  
VOLUME ["/git","/logs"]  
#create the pull script so it can be called when container starts  
ADD git-* /  
RUN chmod +x git-*  
RUN /bin/bash -c './git-setup' #this schedules a cron to pick up once repo is
specified  
ENTRYPOINT ["crond","-l2", "-f"]  

