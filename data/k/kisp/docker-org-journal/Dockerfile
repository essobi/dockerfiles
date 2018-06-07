FROM alpine:latest  
  
RUN apk add --no-cache emacs  
RUN apk add --no-cache ca-certificates  
  
ADD .emacs /root/.emacs  
  
RUN emacs --batch --load /root/.emacs -f package-refresh-contents --eval
"(package-install 'org-journal)"  
  

