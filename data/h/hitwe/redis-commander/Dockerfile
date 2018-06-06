FROM alpine:latest  
  
MAINTAINER Marko OS  
  
ENV TERM=xterm-color  
  
RUN apk --update add bash coreutils curl figlet nano procps tar wget nodejs
nodejs-npm && \  
rm -rf /var/cache/apk/*  
  
CMD ["/bin/bash"]  
  
# Install node packages.  
RUN npm install -g redis-commander  
RUN echo '{}' > /root/.redis-commander  
  
# Define the entrypoint script.  
ENTRYPOINT ["redis-commander"]  
  
# Expose ports.  
EXPOSE 8081  

