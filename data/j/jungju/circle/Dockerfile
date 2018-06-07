FROM library/golang  
  
# Godep for vendoring  
RUN go get -u github.com/tools/godep  
  
# Recompile the standard library without CGO  
RUN CGO_ENABLED=0 go install -a std  
  
ENV APP_DIR $GOPATH/src/github.com/jungju/circle  
RUN mkdir -p $APP_DIR  
  
# Set the entrypoint  
ENTRYPOINT (cd $APP_DIR && ./circle)  
  
ADD . $APP_DIR  
  
# Compile the binary and statically link  
RUN cd $APP_DIR && CGO_ENABLED=0 godep go build -tags 'bindatafs' -ldflags '-d
-w -s' -o circle  
  
EXPOSE 8080

