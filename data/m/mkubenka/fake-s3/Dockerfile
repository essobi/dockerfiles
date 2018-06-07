FROM alpine:3.5  
ENV FAKES3_VERSION 1.0.0  
RUN apk add --no-cache ca-certificates \  
ruby \  
ruby-io-console \  
groff \  
less \  
python \  
py-pip \  
&& gem install --no-rdoc --no-ri fakes3 -v ${FAKES3_VERSION} \  
&& pip install awscli \  
&& apk --purge -v del py-pip \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p /opt/fakes3/data  
  
WORKDIR /opt/fakes3/data  
VOLUME /opt/fakes3/data  
  
COPY docker-entrypoint.sh /  
  
EXPOSE ${FAKES3_PORT:-4569}  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["-r", "/opt/fakes3/data"]  

