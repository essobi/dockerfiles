FROM alpine:latest  
  
WORKDIR /tests/  
ENV ROUNDUP_VERSION v0.0.5  
RUN apk update \  
&& apk add \  
'ncurses' \  
&& apk add --virtual buildDeps \  
'curl' \  
'make' \  
&& curl -L https://github.com/bmizerany/roundup/tarball/${ROUNDUP_VERSION} |
tar xvzf - \  
&& cd bmizerany-roundup-* && ./configure && make && make install && cd .. \  
&& rm -r bmizerany-roundup-* \  
&& apk del buildDeps \  
&& rm -rf /var/cache/apk/*  
  
COPY run-tests.sh /app/  
COPY links.txt /tests/  
  
CMD ["/app/run-tests.sh"]  

