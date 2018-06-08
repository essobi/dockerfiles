# ------------------------------------------------  
# Builder image  
# ------------------------------------------------  
FROM thumbsupgallery/runtime:alpine as build  
  
# Standard build dependencies for <npm install>  
RUN apk add --no-cache git make g++ python bash  
  
# Install thumbsup locally  
WORKDIR /thumbsup  
COPY VERSION VERSION  
RUN echo "Installing thumbsup@$(cat VERSION)"  
RUN npm install thumbsup@$(cat VERSION)  
  
# ------------------------------------------------  
# Runtime image  
# ------------------------------------------------  
FROM thumbsupgallery/runtime:alpine  
  
# Use tini as an init process  
# to ensure all child processes (ffmpeg...) are always terminated properly  
RUN apk add --update tini  
ENTRYPOINT ["tini", "-g", "--"]  
  
# Copy the thumbsup files to the new image  
COPY \--from=build /thumbsup /thumbsup  
RUN ln -s /thumbsup/node_modules/.bin/thumbsup /usr/local/bin/thumbsup  
  
# Default command, should be overridden during <docker run>  
CMD ["thumbsup"]  

