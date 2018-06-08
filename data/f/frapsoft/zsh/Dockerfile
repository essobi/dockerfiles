FROM alpine  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
RUN apk update && \  
apk add --no-cache zsh && \  
rm -f /tmp/* /etc/apk/cache/*  
  
RUN sed -i -e "s/bin\/ash/bin\/zsh/" /etc/passwd  
  
ENV SHELL /bin/zsh  
  
CMD ["zsh", "--version"]  

