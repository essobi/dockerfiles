FROM luckyqm/golang:alpine  
LABEL MAINTAINER QiMa "mq@luckyzune.com"  
LABEL builder_version="8.5.23"  
  
# 更新常用的go lib  
RUN go get github.com/axgle/mahonia  
RUN go get github.com/chanxuehong/rand  
RUN go get github.com/golang/protobuf/proto  
RUN go get github.com/gorilla/websocket  
RUN go get github.com/labstack/gommon/log  
RUN go get github.com/op/go-logging  
RUN go get github.com/tealeg/xlsx  
RUN go get github.com/spf13/cobra  
RUN go get github.com/spf13/viper  
RUN go get github.com/kataras/iris  
RUN go get github.com/eclipse/paho.mqtt.golang  
RUN go get github.com/go-pg/pg  
RUN go get github.com/streadway/amqp  
RUN go get github.com/garyburd/redigo/redis  
  
RUN go get golang.org/x/net/http2  
RUN go get gopkg.in/chanxuehong/wechat.v2  
RUN go get gopkg.in/yaml.v2  
RUN go get gopkg.in/mgo.v2  
RUN go get github.com/opentracing/opentracing-go  
  
#8.3.20  
RUN go get sourcegraph.com/sourcegraph/appdash  
  
#8.3.23  
RUN go get github.com/dinever/golf  
  
#8.4.24  
RUN go get github.com/satori/go.uuid  
RUN go get github.com/juju/errors  
RUN go get github.com/go-xorm/core  
RUN go get github.com/go-xorm/xorm  
RUN go get github.com/lib/pq  
  
#8.4.25  
RUN go get github.com/go-xorm/builder  
RUN go get github.com/rs/cors  
RUN go get github.com/chanxuehong/util  
RUN go get github.com/bitly/go-simplejson  
  
#8.4.26  
RUN go get github.com/mholt/archiver  
RUN go get github.com/gomodule/redigo/...  
  
#8.4.30  
RUN go get gonum.org/v1/gonum/...  
RUN go get github.com/kniren/gota/...  
  
#8.5.3  
RUN go get github.com/emirpasic/gods/...  
RUN go get github.com/ulikunitz/xz  
RUN go get github.com/pierrec/xxHash/...  
RUN go get github.com/pierrec/lz4  
RUN go get github.com/nwaples/rardecode  
RUN go get github.com/golang/snappy  
RUN go get github.com/dsnet/compress  
  
#8.5.18  
RUN go get github.com/Sirupsen/logrus  
RUN go get golang.org/x/net/webdav  
  
#8.5.22  
RUN go get github.com/asdine/storm  
RUN go get github.com/coreos/bbolt  
RUN go get github.com/hacdias/fileutils  
RUN go get gopkg.in/natefinch/lumberjack.v2  
RUN go get github.com/GeertJohan/go.rice  
RUN go get github.com/daaku/go.zipexe  
RUN go get github.com/kardianos/osext  
RUN go get github.com/gohugoio/hugo  
RUN go get github.com/BurntSushi/toml  
RUN go get github.com/chaseadamsio/goorgeous  
RUN go get github.com/russross/blackfriday  
RUN go get github.com/shurcooL/sanitized_anchor_name  
RUN go get github.com/PuerkitoBio/purell  
RUN go get github.com/PuerkitoBio/urlesc  
RUN go get github.com/alecthomas/chroma  
RUN go get github.com/mholt/caddy  
RUN go get github.com/robfig/cron  
RUN go get github.com/dgrijalva/jwt-go  
RUN go get github.com/hacdias/varutils  
RUN go get github.com/flynn/go-shlex  
RUN go get github.com/google/uuid  
RUN go get github.com/robfig/cron  
RUN go get golang.org/x/crypto/blowfish  
RUN go get github.com/dgrijalva/jwt-go/request  
RUN go get golang.org/x/crypto/bcrypt  
  
#8.5.23  
RUN go get github.com/abiosoft/caddyplug  
RUN go get github.com/abiosoft/errs  
RUN go get github.com/fatih/color  
RUN go get github.com/abiosoft/errs  
RUN go get github.com/abiosoft/caddyplug/internal  
RUN go get github.com/fatih/color/vendor/github.com/mattn/go-isatty  
RUN go get github.com/fatih/color/vendor/github.com/mattn/go-colorable  
RUN go get github.com/fatih/color  
RUN go get github.com/abiosoft/caddyplug/caddyplug  
RUN go get github.com/hashicorp/go-syslog  
RUN go get github.com/bifurcation/mint/syntax  
RUN go get golang.org/x/crypto/curve25519  
RUN go get golang.org/x/crypto/hkdf  
RUN go get github.com/lucas-clemente/quic-go  
RUN go get github.com/hashicorp/golang-lru/simplelru  
RUN go get github.com/lucas-clemente/aes12  
RUN go get github.com/hashicorp/golang-lru  
RUN go get golang.org/x/text/transform  
RUN go get github.com/lucas-clemente/quic-go  
RUN go get github.com/russross/blackfriday  
RUN go get gopkg.in/natefinch/lumberjack.v2  
RUN go get github.com/lucas-clemente/quic-go/h2quic  
RUN go get github.com/xenolf/lego/...  
  
WORKDIR /go/src/github.com/luckyzune/golang/  
  
RUN mkdir -p /root/.ssh/  
COPY builder/id_rsa /root/.ssh/id_rsa  
COPY builder/id_rsa.pub /root/.ssh/id_rsa.pub  
COPY builder/.gitconfig /root/.gitconfig  
  
RUN chmod 600 /root/.ssh/id_rsa  
  
RUN mkdir -p /etc/ssh/  
RUN echo 'IdentityFile ~/.ssh/id_rsa' >> /etc/ssh/ssh_config  
RUN sed -i 's/# StrictHostKeyChecking ask/StrictHostKeyChecking no/'
/etc/ssh/ssh_config  

