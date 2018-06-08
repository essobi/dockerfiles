FROM gliderlabs/alpine:3.1  
MAINTAINER Nick Schuch  
  
RUN apk --update add ca-certificates curl  
  
RUN curl -L https://github.com/previousnext/ecs-
reaper/releases/download/0.0.4/ecs-reaper-linux-amd64 -o /usr/local/bin/ecs-
reaper && \  
chmod +rx /usr/local/bin/ecs-reaper  
  
CMD ["ecs-reaper"]  

