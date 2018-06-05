FROM diegoteam/diego-cli:latest  
  
MAINTAINER Roberto Jimenez Sanchez, <jszroberto@gmail.com>  
  
RUN /bin/bash -l -c "go get -t -v github.com/cloudfoundry-incubator/diego-
acceptance-tests/..."  
  
ADD bin/* /root/bin/  
RUN chmod +x /root/bin/*  
  
RUN /bin/bash -l -c "go install -v github.com/onsi/ginkgo/ginkgo"  
  
ENV DATSDIR /root/go/src/github.com/cloudfoundry-incubator/diego-acceptance-
tests  
#ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
ENTRYPOINT bash -l -c "load.env run.dats"  

