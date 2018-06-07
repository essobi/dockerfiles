FROM golang  
MAINTAINER Love Nyberg <love.nyberg@lovemusic.se> (@jacksoncage)  
EXPOSE 8010-8100  
ENV APPPATH $GOPATH/src/github.com/jacksoncage/munin_exporter  
COPY . $APPPATH  
RUN cd $APPPATH && go get -d && go build -o /bin/munin_exporter \  
&& mv $APPPATH/start /opt/munin_exporter && rm -rf $GOPATH  
WORKDIR /opt  
  
CMD ["bash", "/opt/munin_exporter"]  

