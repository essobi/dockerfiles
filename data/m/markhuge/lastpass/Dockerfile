# Lastpass cli  
#  
# Usage:  
# lpass () {  
# docker run -it --rm \  
# -v /etc/localtime:/etc/localtime \  
# -v $HOME/.lpass:/root/.lpass \  
# markhuge/lastpass "$@"  
# }  
FROM alpine:edge  
MAINTAINER Mark Wilkerson <mark@markwilkerson.me>  
  
RUN apk --no-cache add \  
ca-certificates openssl-dev git gcc g++ automake make curl-dev \  
libxml2-dev  
  
RUN git clone https://github.com/LastPass/lastpass-cli.git /usr/src/lastpass-
cli  
  
WORKDIR /usr/src/lastpass-cli  
  
RUN make && make install  
  
ENTRYPOINT ["lpass"]  
  

