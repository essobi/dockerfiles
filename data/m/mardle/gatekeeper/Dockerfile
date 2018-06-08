FROM alpine:3.4  
ENV BUILD_PACKAGES curl-dev ruby-dev build-base  
  
# Update and install base packages  
RUN apk update && apk upgrade && apk add bash $BUILD_PACKAGES  
# Install ruby and ruby-bundler  
RUN apk add ruby ruby-io-console ruby-bundler  
  
RUN echo 'gem: --no-document --no-ri --no-rdoc' > /etc/gemrc  
  
# Clean APK cache  
RUN rm -rf /var/cache/apk/*  
  
# Make and copy the application  
RUN mkdir /app  
ADD . /app  
WORKDIR /app  
RUN chmod +x bin/gatekeeper  
# Make sure all gems are there  
RUN bundler install  
# Run the application  
CMD ["ruby", "bin/gatekeeper"]  

