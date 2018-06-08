FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
gcc g++ libc6-dev make golang \  
git git-annex openssh-server \  
python-pip python-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
RUN apt-get install -y golang  
ENV GOPATH /opt/go/  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 755 "$GOPATH"  
WORKDIR $GOPATH  
  
RUN mkdir -p src/github.com/G-Node/gin-auth/  
ADD ./ src/github.com/G-Node/gin-auth/  
ADD ./conf src/github.com/G-Node/gin-auth/conf/  
  
RUN go get github.com/G-Node/gin-core/gin  
RUN go get github.com/NYTimes/logrotate  
RUN go get github.com/Sirupsen/logrus  
RUN go get github.com/dchest/captcha  
RUN go get github.com/docopt/docopt-go  
RUN go get github.com/gorilla/handlers  
RUN go get github.com/gorilla/mux  
RUN go get github.com/jmoiron/sqlx  
RUN go get github.com/lib/pq  
RUN go get github.com/pborman/uuid  
RUN go get golang.org/x/crypto/bcrypt  
RUN go get golang.org/x/crypto/ssh  
RUN go get gopkg.in/yaml.v2  
  
WORKDIR $GOPATH/src/github.com/G-Node/gin-auth/  
  
VOLUME /conf  
VOLUME /authlog  
  
RUN go install  
  
WORKDIR /wd  
  
EXPOSE 8081  
ENTRYPOINT $GOPATH/bin/gin-auth --conf /conf  
  

