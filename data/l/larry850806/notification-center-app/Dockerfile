FROM larry850806/golang-workspace  
  
COPY src/main/*.go src/main/Gopkg* src/main/Makefile /root/workspace/src/main/  
  
WORKDIR /root/workspace/src/main  
  
# install dependencies, build and remove cache  
RUN dep ensure && \  
go build && \  
rm -rf *.go Gopkg* Makefile vendor && \  
rm -rf ../../pkg  
  
CMD ["./main"]

