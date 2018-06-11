FROM larry850806/workspace-base  
  
# get go binary file from official  
RUN wget https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz && \  
tar -xvf go1.9.2.linux-amd64.tar.gz && \  
mv go / && \  
rm go1.9.2.linux-amd64.tar.gz  
  
# set initial gopath  
ENV GOPATH /go  
# set path to go binary  
ENV PATH "/go/bin:${PATH}"  
  
# install glide  
RUN curl https://glide.sh/get | sh  
  
# install dep  
RUN wget https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-
amd64 && \  
chmod u+x dep-linux-amd64 && \  
mv dep-linux-amd64 /go/bin/dep  
  
ENV GOPATH /root/workspace

