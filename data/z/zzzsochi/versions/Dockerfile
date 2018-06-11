FROM alpine  
LABEL maintainer="Alexander Zelenyak <zzz.sochi@gmail.com>"  
WORKDIR /srv/src  
COPY . /srv/src  
RUN apk add --no-cache rust cargo  
RUN cargo build --release  
  
FROM alpine  
LABEL maintainer="Alexander Zelenyak <zzz.sochi@gmail.com>"  
RUN apk add --no-cache libgcc  
COPY \--from=0 /srv/src/target/release/versions /usr/bin/versions  
ENTRYPOINT ["/usr/bin/versions"]  

