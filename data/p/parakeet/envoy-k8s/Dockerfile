FROM envoyproxy/envoy-alpine:9ed62923a8ff6745407046c4451ce757348d966f  
  
RUN apk add --no-cache python  
ADD restarter.py /usr/local/bin/envoy-restarter.py  
RUN chmod ugo+x /usr/local/bin/envoy-restarter.py  
  
ENTRYPOINT ["/usr/local/bin/envoy-restarter.py"]

