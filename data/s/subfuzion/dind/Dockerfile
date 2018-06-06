FROM docker:17.07-rc-dind  
RUN apk --no-cache add iproute2 bind-tools drill  
ENV DOCKER_HIDE_LEGACY_COMMANDS=1  
ENTRYPOINT ["dockerd-entrypoint.sh", "--experimental"]  
CMD []  
  

