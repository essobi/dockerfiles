FROM youske/alpine-nodejs:latest  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.stdmachine.description="alpine netdata image" \  
com.stdmachine.role="netdata image"  
  
ENV PORT=19999 \  
SECONDS=1  
RUN addgroup -S netdata && adduser -D -H -G netdata netdata && \  
apk add gawk curl jq libuuid --no-cache && \  
apk add git zlib-dev automake autoconf build-base linux-headers musl-dev util-
linux-dev libmnl-dev -t buildpack --no-cache && \  
cd /tmp && git clone https://github.com/firehol/netdata.git --depth=1 && \  
cd netdata && ./netdata-installer.sh --dont-wait && \  
apk del buildpack --purge --no-cache && rm -rf /tmp/* /var/apk/cache*
/root/.wget-htst  
  
EXPOSE ${PORT}  
CMD ["/usr/sbin/netdata", "-D","-t","${SECONDS}","-p","${PORT}"]  

