FROM larry850806/golang-workspace  
  
COPY src/main/*.go src/main/Gopkg* src/main/Makefile /root/workspace/src/main/  
  
WORKDIR /root/workspace/src/main  
  
# set path and install dependencies  
RUN cd /root/workspace/src/main && \  
dep ensure && \  
go build && \  
rm -rf Gopkg.* Makefile *.go vendor ../../pkg  
  
CMD ["./main"]

