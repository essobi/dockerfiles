FROM docker.io/rvsingh/centosgo5:latest  
RUN echo "export PATH=$PATH:/usr/local/go/bin" > /etc/profile.d/path.sh  
RUN echo "export GOBIN=$HOME/bin" >> /.bash_profile  
RUN echo "export GOPATH=$HOME/src" >> /.bash_profile  
RUN source /etc/profile && source /.bash_profile  
COPY WebApp.go /projects/src/WebApp.go  
EXPOSE 9090  
CMD ["usr/local/go/bin/go","run","/projects/src/WebApp.go"]  
  

