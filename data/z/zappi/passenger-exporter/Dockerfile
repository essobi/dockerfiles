FROM ruby:2.4.3-alpine3.7  
ARG GOLANG_VERSION="1.9.2-r1"  
ARG BUILD_DEPS="go=$GOLANG_VERSION ruby-dev linux-headers curl curl-dev pcre-
dev libexecinfo-dev@edge-main"  
ARG RUNTIME_DEPS="tini build-base pcre git libexecinfo@edge-main"  
RUN echo '@edge-main http://dl-cdn.alpinelinux.org/alpine/edge/main/' >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade && \  
apk add $BUILD_DEPS && \  
apk add $RUNTIME_DEPS && \  
mkdir -p /opt  
  
# Passenger  
ENV PASSENGER_VERSION="5.1.12" \  
PATH="/opt/passenger/bin:$PATH"  
RUN curl -L "https://s3.amazonaws.com/phusion-
passenger/releases/passenger-$PASSENGER_VERSION.tar.gz" | tar -xzf - -C /opt
&& \  
mv /opt/passenger-$PASSENGER_VERSION /opt/passenger && \  
passenger-config validate-install --auto && \  
export EXTRA_PRE_CFLAGS='-O' EXTRA_PRE_CXXFLAGS='-O'
EXTRA_LDFLAGS='-lexecinfo' && \  
passenger-config compile-agent --optimize && \  
passenger-config install-standalone-runtime && \  
passenger-config build-native-support  
  
# Go configuration  
ENV GOROOT="/usr/lib/go" \  
GOPATH="/go"  
ENV PATH="$GOPATH/bin:$GOROOT/bin:$PATH"  
# Go dependencies  
RUN go get github.com/prometheus/promu  
  
# Configure source path  
ARG SOURCE_PATH="/go/src/github.com/Intellection/passenger-exporter"  
RUN mkdir -p ${SOURCE_PATH}  
  
# Add source files  
ADD . ${SOURCE_PATH}/  
WORKDIR ${SOURCE_PATH}  
  
# Build exporter  
RUN promu build && \  
mv ${SOURCE_PATH}/passenger-exporter /usr/local/bin/passenger-exporter && \  
rm -rf ${SOURCE_PATH}/*  
  
# Cleanup  
RUN apk del $BUILD_PACKAGES && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["tini", "--", "passenger-exporter"]  
CMD ["/bin/sh"]  

