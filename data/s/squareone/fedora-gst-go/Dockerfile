FROM fedora:25  
RUN dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-
release-$(rpm -E %fedora).noarch.rpm
https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm
-E %fedora).noarch.rpm && \  
dnf install -y gstreamer1 gstreamer1-plugins-good gstreamer1-libav tar git
mercurial  
  
RUN mkdir /goroot && curl https://storage.googleapis.com/golang/go1.7.5.linux-
amd64.tar.gz | tar xvzf - -C /goroot --strip-components=1  
  
RUN mkdir /gopath  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
ADD go-build /bin/go-build  
ADD go-run /bin/go-run  
  
ONBUILD ADD . /gopath/src/app/  
ONBUILD RUN /bin/go-build  
  
CMD []  
  
ENTRYPOINT ["/bin/go-run"]  

