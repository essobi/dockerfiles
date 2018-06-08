FROM google/golang  
RUN go get -v code.google.com/p/go.tools/cmd/present  
ONBUILD ADD . /slides  
WORKDIR /slides  
EXPOSE 3999  
ENTRYPOINT ["/gopath/bin/present"]  
CMD ["-http", "0.0.0.0:3999"]  

