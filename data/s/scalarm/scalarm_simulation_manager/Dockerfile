FROM centos:7  
SHELL ["/bin/bash", "-l", "-c"]  
ENV SCALARM_HOME /scalarm  
RUN yum install -y curl git  
WORKDIR /tmp  
RUN curl -LO https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz  
RUN tar -C /usr/local -xvzf go1.8.3.linux-amd64.tar.gz  
ENV PATH $PATH:/usr/local/go/bin  
ENV GOROOT /usr/local/go  
ENV GOPATH $SCALARM_HOME  
RUN go get github.com/scalarm/scalarm_simulation_manager_go  
RUN go install github.com/scalarm/scalarm_simulation_manager_go  
WORKDIR $SCALARM_HOME/bin  
RUN ln -s /usr/bin/python2 /usr/bin/python2.6  
CMD /bin/bash -l -c ./scalarm_simulation_manager_go  

