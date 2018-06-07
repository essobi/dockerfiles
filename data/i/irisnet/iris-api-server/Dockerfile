# docker usage  
# docker build -t iris-api:v1 .  
# docker run --name iris-api-server -v /mnt/data/iris-log:/iris-api/log -p
9080:9080 -e "DB_HOST=127.0.0.1" -e "DB_PORT=27117" -e "ENV=stage" -d iris-
api:v1  
FROM alpine:edge  
  
# Set up dependencies  
ENV PACKAGES go make git libc-dev bash  
  
# Set up GOPATH & PATH  
ENV GOPATH /root/go  
ENV BASE_PATH $GOPATH/src/github.com/irisnet  
ENV REPO_PATH $BASE_PATH/iris-api-server  
ENV LOG_DIR /iris-api/log  
ENV PATH $GOPATH/bin:$PATH  
ENV API_PORT 9080  
# Set volumes  
VOLUME $LOG_DIR:api-log  
  
# Link expected Go repo path  
RUN mkdir -p $LOG_DIR $GOPATH/pkg $GOPATH/bin $BASE_PATH $REPO_PATH  
  
# Add source files  
COPY . $REPO_PATH  
  
# Install minimum necessary dependencies, build iris-api-server  
RUN apk add --no-cache $PACKAGES && \  
cd $REPO_PATH && make all && \  
mv $REPO_PATH/iris-api $GOPATH/bin && \  
rm -rf $REPO_PATH/vendor && \  
rm -rf $GOPATH/src/github.com/golang $GOPATH/bin/dep $GOPATH/pkg/* && \  
apk del $PACKAGES  
  
VOLUME ["$LOG_DIR"]  
  
EXPOSE $API_PORT  
  
CMD iris-api > $LOG_DIR/debug.log && tail -f $LOG_DIR/debug.log

