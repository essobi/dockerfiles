FROM thinca/vim  
  
ENV REVIEWDOG_VERSION 0.9.8  
ENV REVIEWDOG_URL
https://github.com/haya14busa/reviewdog/releases/download/$REVIEWDOG_VERSION/reviewdog_linux_amd64  
ENV VINT_VERSION 0.3.17  
RUN apk --update --no-cache add \  
ca-certificates \  
curl \  
git \  
python3 \  
go  
  
# make golang binary executable  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
  
# reviewdog  
RUN curl -fSL $REVIEWDOG_URL -o /usr/local/bin/reviewdog && chmod +x
/usr/local/bin/reviewdog  
  
# vint  
RUN pip3 install --upgrade pip \  
&& pip3 install vim-vint==$VINT_VERSION \  
&& rm -r /root/.cache  
  
# vim-vimlint  
RUN git -c advice.detachedHead=false clone https://github.com/syngan/vim-
vimlint --quiet --depth 1 /vim-vimlint \  
&& git -c advice.detachedHead=false clone https://github.com/ynkdir/vim-
vimlparser --quiet --depth 1 /vim-vimlparser  
COPY ./vimlint /usr/local/bin/vimlint  
  
# for golang linter script using go-vimlparser  
RUN mkdir /go  
ENV GOPATH /go  

