FROM philippwaller/golang:latest  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="Watchtower" \  
org.label-schema.description="Watchtower"  
  
ENV WATCHTOWER_PATH=github.com/v2tec/watchtower  
ENV WATCHTOWER_REPO=https://${WATCHTOWER_PATH}.git \  
WATCHTOWER_BRANCH=master  
  
RUN apt-get update \  
&& apt-get install -y gcc git \  
&& go get -u github.com/Masterminds/glide \  
&& git clone -b ${WATCHTOWER_BRANCH} ${WATCHTOWER_REPO}
/usr/local/src/${WATCHTOWER_PATH} \  
&& cd /usr/local/src/${WATCHTOWER_PATH} \  
&& glide install \  
&& go install ${WATCHTOWER_PATH} \  
&& ln -s /usr/local/bin/watchtower /usr/bin/ \  
&& apt-get autoremove -y gcc git \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
ENTRYPOINT ["/usr/bin/watchtower"]  
CMD ["--help"]  

