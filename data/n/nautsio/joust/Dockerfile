FROM golang:1.7-alpine  
  
# Install python in order to use the gae sdk, curl to fetch it and unzip to
extract it.  
RUN apk --no-cache add python curl git unzip  
  
# Install gb and gb-gae to build and deploy our application.  
RUN go get github.com/constabulary/gb/... && \  
go get code.palmstonegames.com/gb-gae  
  
# Install the gae sdk.  
RUN cd / && \  
curl -s https://storage.googleapis.com/appengine-
sdks/featured/go_appengine_sdk_linux_amd64-1.9.38.zip -o appengine.zip && \  
unzip appengine.zip && \  
mv go_appengine gae && \  
rm appengine.zip  
  
# Add gae sdk to the path so we can run goapp.  
ENV PATH=$PATH:/gae  
  
# Build everything in /build.  
WORKDIR /build  
VOLUME /build  
  
# Expose the local gae server and admin interface.  
EXPOSE 8080 8000  
ENTRYPOINT ["gb"]  

