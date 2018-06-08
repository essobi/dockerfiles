FROM alpine  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
RUN apk update && \  
apk add --no-cache fish && \  
rm -f /tmp/* /etc/apk/cache/*  
  
RUN sed -i -e "s/bin\/ash/usr\/bin\/fish/" /etc/passwd  
  
ENV SHELL /usr/bin/fish  
  
CMD ["fish", "--version"]  

