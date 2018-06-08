FROM golang  
  
# dependencies  
RUN apt-get update  
RUN apt-get install -y pkg-config libzmq3-dev build-essential python3-pip  
  
# set up golang  
ENV PATH /usr/local/go/bin:$PATH  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:$PATH  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
# install gophernotes  
RUN go get golang.org/x/tools/cmd/goimports  
RUN go get -tags zmq_3_x github.com/gopherds/gophernotes  
RUN mkdir -p ~/.ipython/kernels/gophernotes  
RUN cp -r $GOPATH/src/github.com/gopherds/gophernotes/kernel/*
~/.ipython/kernels/gophernotes  
  
# Install Tini  
RUN curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini >
tini && \  
echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# install jupyter  
RUN pip3 install --upgrade pip && \  
pip3 install -vU setuptools && \  
pip3 install jupyter  
#mkdir /mnt/notebooks  
VOLUME /mnt/notebooks  
WORKDIR /  
  
EXPOSE 8888  
ENTRYPOINT ["tini", "--"]  
CMD ["jupyter", "notebook", "--allow-root", "--no-browser", "--ip=0.0.0.0", "
--notebook-dir=/mnt/notebooks", "--NotebookApp.token=''"]  

