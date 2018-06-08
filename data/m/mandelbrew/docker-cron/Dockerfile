FROM alpine:latest  
MAINTAINER Carlos Avila "cavila@mandelbrew.com"  
# Prep env  
ENV PYTHONUNBUFFERED 1  
ENV PRE_RESOURCES_HOOK ''  
ENV RESOURCES_URL ''  
ENV POST_RESOURCES_HOOK ''  
# Operating System  
RUN apk update \  
&& apk add --no-cache \  
curl  
  
# Application  
WORKDIR /root  
  
ADD scripts/docker-cmd.sh docker-cmd.sh  
RUN chmod +x docker-cmd.sh  
  
CMD ["./docker-cmd.sh"]

