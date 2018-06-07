FROM diegoteam/bosh-cli  
MAINTAINER Roberto Jimenez Sanchez, <jszroberto@gmail.com>  
# Installation of Bosh CLI  
# Installation of CF CLI and Spiff  
RUN wget https://github.com/cloudfoundry-
incubator/spiff/releases/download/v1.0.7/spiff_linux_amd64.zip && unzip -d
/usr/local/bin/ spiff_linux_amd64.zip && rm spiff_linux_amd64.zip  
  
RUN wget
'https://cli.run.pivotal.io/stable?release=linux64-binary&source=github' && mv
'stable?release=linux64-binary&source=github' cf.tar.gz && tar -xf cf.tar.gz
-C /usr/local/bin/ && rm cf.tar.gz  
  
# Installation of GO  
RUN wget https://storage.googleapis.com/golang/go1.5.3.linux-amd64.tar.gz -P
/tmp  
RUN tar -C /usr/local -xvf /tmp/go1.5.3.linux-amd64.tar.gz  
RUN ln /usr/local/go/bin/go /usr/bin/go  
  
ENV GOPATH /root/go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
ENV CFDIR /root/cf-release  
  
RUN git clone https://github.com/cloudfoundry/cf-release.git /root/cf-release  
  
ADD bin/* /root/bin/  
RUN chmod +x /root/bin/*  
  
CMD bash -l -c "load.env"  

