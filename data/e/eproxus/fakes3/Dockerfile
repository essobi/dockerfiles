FROM alpine:edge  
  
ENV FAKES3_VERSION 0.2.1  
RUN apk add --update \  
ruby \  
ruby-io-console \  
&& \  
rm -rf /var/cache/apk/* && \  
gem install --no-rdoc --no-ri fakes3 -v ${FAKES3_VERSION} && \  
mkdir -p /srv/fakes3  
  
VOLUME /srv/fakes3  
WORKDIR /srv/fakes3  
EXPOSE 80  
ENTRYPOINT ["/usr/bin/fakes3"]  
CMD ["-r", "/srv/fakes3", "-p", "80"]  

