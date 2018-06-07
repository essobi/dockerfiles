FROM alpine:3.7  
ENV USERNAME __fossil  
  
RUN addgroup -Sg 400 g$USERNAME \  
&& adduser -Su 400 -G g$USERNAME $USERNAME \  
&& apk add --no-cache alpine-sdk zlib-dev openssl-dev tcl fossil \  
&& mkdir -p /usr/local/src/fossils/fossil/build \  
&& cd /usr/local/src/fossils \  
&& fossil clone http://www.fossil-scm.org/fossil fossil.fossil --user
$USERNAME \  
&& cd fossil \  
&& fossil open ../fossil.fossil \  
&& cd build \  
&& ../configure --static \  
&& make \  
&& make install \  
&& cd /tmp \  
&& rm -fr /usr/local/src \  
&& apk del --purge --no-cache fossil alpine-sdk zlib-dev openssl-dev tcl \  
&& rm -f /var/cache/apk/*  
  
VOLUME ["/fossils"]  
  
WORKDIR ["/fossils"]  
  
EXPOSE 8181  
ENTRYPOINT ["/usr/local/bin/fossil"]  
  
CMD ["server","--repolist","--port","8181","--skin","ardoise","/fossils"]  

