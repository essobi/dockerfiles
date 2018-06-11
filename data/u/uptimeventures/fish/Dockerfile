FROM
alpine:3.7@sha256:7df6db5aa61ae9480f52f0b3a06a140ab98d427f86d8d5de0bedab9b8df6b1c0  
MAINTAINER Nicholas Young <nyoung@uptime.ventures>  
RUN apk add --update --no-cache fish && \  
sed -i -e "s/bin\/ash/usr\/bin\/fish/" /etc/passwd  
ENV SHELL=fish  
CMD ["fish", "--version"]  

