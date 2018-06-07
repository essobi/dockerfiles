FROM golang:1.7  
ENV GB_VERSION 0.4.3  
ENV GB_ERRORS_VERSION 0.7.1  
RUN set -x \  
&& export GOPATH="$(mktemp -d)" \  
\  
&& mkdir -p "$GOPATH/src/github.com/pkg/errors" \  
&& cd "$GOPATH/src/github.com/pkg/errors" \  
&& wget -qO-
"https://github.com/pkg/errors/archive/v${GB_ERRORS_VERSION}.tar.gz" \  
| tar -xz --strip-components=1 \  
&& go install -v ./... \  
\  
&& mkdir -p "$GOPATH/src/github.com/constabulary/gb" \  
&& cd "$GOPATH/src/github.com/constabulary/gb" \  
&& wget -qO-
"https://github.com/constabulary/gb/archive/v${GB_VERSION}.tar.gz" \  
| tar -xz --strip-components=1 \  
&& go install -v ./... \  
\  
&& cd "$GOPATH/bin" \  
&& cp -Rv . /usr/local/bin/ \  
\  
&& cd \  
&& rm -rf "$GOPATH"  
  
ENV PATH /usr/src/uscan-helper/bin:$PATH  
WORKDIR /usr/src/uscan-helper  
  
COPY . .  
  
RUN gb build  
  
EXPOSE 8181  
CMD ["uscan-helper"]  

