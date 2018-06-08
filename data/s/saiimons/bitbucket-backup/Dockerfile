FROM 'alpine:3.7'  
RUN apk update && apk add jq curl git mercurial openssh  
  
COPY bitbucket_backup.sh /entrypoint.sh  
  
CMD /entrypoint.sh  

