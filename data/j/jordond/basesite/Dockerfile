# Simple docker container for my websites  
#  
# Clones the repo and runs 'npm run build'  
#  
# ENV Variables  
# repo - Repository to clone ex: <:user>/<:repo>  
# branch - Branch to checkout ex: <:branch> \- defaults to master  
#  
# Example:  
# docker run -d \  
# --name=hoogit \  
# --restart=always \  
# -p 9400:8080 \  
# -e repo=jordond/hoogit \  
# -e branch=master  
# jordond/baseSite  
FROM node:5-wheezy  
  
ENV SOURCE_DIR /usr/src  
  
ADD ./start.sh /start.sh  
ADD ./build-project /build-project  
RUN chmod u+x /start.sh  
RUN chmod u+x /build-project  
  
RUN mkdir -p /usr/src  
WORKDIR /usr/src  
  
EXPOSE 8080  
CMD [ "/start.sh" ]

