FROM alpine  
RUN apk add --update --no-cache perl mercurial ca-certificates && mkdir -p
/opt/work && cd /opt/work && hg clone https://bitbucket.org/topia/tiarra  
WORKDIR /opt/work/tiarra  
CMD ./tiarra --config=tiarra.conf  

