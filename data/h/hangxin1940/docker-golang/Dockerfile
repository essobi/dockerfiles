#  
# golang  
#  
# https://github.com/hangxin1940/docker-golang  
#  
  
# Pull base image.  
FROM dockerfile/ubuntu  
  
ENV GOROOT /usr/local/go  
ENV GOPATH /home/go  
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH  
  
# Install golang.  
RUN \  
cd /tmp && \  
wget https://godeb.s3.amazonaws.com/godeb-amd64.tar.gz && \  
tar xvzf godeb-amd64.tar.gz && \  
./godeb install && \  
rm -rf /tmp/go* && \  
mkdir /home/go && \  
go get github.com/revel/revel && \  
go get github.com/revel/cmd/revel && \  
go get gopkg.in/mgo.v2 && \  
go get google.golang.org/grpc && \  
go get github.com/nu7hatch/gouuid && \  
go get github.com/kaz8/go-captcha && \  
go get github.com/gogap/luosimao && \  
go get github.com/garyburd/redigo/redis && \  
go get github.com/hangxin1940/mgorm  
echo "export GOPATH=/home/go" >> ~/.bashrc && \  
echo "export GOROOT=/usr/local/go" >> ~/.bashrc && \  
echo "export PATH=$PATH:$GOROOT/bin:$GOPATH/bin" >> ~/.bashrc  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]  

