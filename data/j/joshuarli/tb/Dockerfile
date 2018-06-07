FROM joshuarli/alpine-usanic  
MAINTAINER joshuarli <joshua.r.li.98@gmail.com>  
  
# Not going to be setting up pipenv in order to have a smaller image.  
# Manually edit this Dockerfile if dependencies change.  
RUN apk add --update --no-cache redis && \  
pip3 install redis --no-cache-dir  
  
WORKDIR /app  
ADD . /app  
# EXPOSE 1337 is already done by alpine-usanic, for sanic.  
EXPOSE 6379  
CMD ["sh", "run.sh"]  

