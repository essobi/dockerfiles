FROM alpine:3.4  
ENV FAKES3_VERSION 0.2.5  
RUN apk add --no-cache ca-certificates ruby ruby-io-console \  
&& rm -rf /var/cache/apk/* \  
&& echo "Installing fakes3, please wait, it can take long time..." \  
&& gem install --no-rdoc --no-ri fakes3 -v ${FAKES3_VERSION} \  
&& mkdir -p /opt/fakes3/data  
  
WORKDIR /opt/fakes3/data  
VOLUME /opt/fakes3/data  
  
EXPOSE 10001  
ENTRYPOINT ["/usr/bin/fakes3", "-r", "/opt/fakes3/data", "-p"]  
CMD ["10001"]  

