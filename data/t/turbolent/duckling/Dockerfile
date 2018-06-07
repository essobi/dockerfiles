FROM alpine  
  
RUN apk add --no-cache curl ghc musl-dev pcre-dev git zlib-dev  
  
RUN curl -sSL https://get.haskellstack.org/ | sh  
  
RUN git clone https://github.com/facebookincubator/duckling.git  
  
WORKDIR /duckling  
  
RUN stack build --system-ghc --copy-bins --local-bin-path /usr/local/bin  
  
FROM alpine  
  
RUN apk add --no-cache pcre zlib gmp libffi tzdata  
  
COPY \--from=0 /usr/local/bin/duckling-example-exe /usr/local/bin/duckling  
  
CMD exec duckling  
  
EXPOSE 8000  

