FROM denismakogon/gocv-alpine:3.4.1-buildstage  
LABEL author="Romel Campbell"  
  
ENV APP_HOME /var/app  
  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
COPY camera.go $APP_HOME  
RUN go build camera.go  
ENV PORT 3000  
EXPOSE 3000  
CMD ["./camera"]

