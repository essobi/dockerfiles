FROM golang:1.9  
RUN apt-get update && apt-get install -y \  
default-jre\  
python-pip  
RUN pip install requests==2.13.0 Faker==0.7.17 nose==1.3.7 psycopg2==2.7.3.1
pytoml==0.1.14 pika==0.11.0 dpath==1.4.0 termcolor==1.1.0  
RUN curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 &&
chmod +x /usr/local/bin/dep  
RUN go get \  
"golang.org/x/net/context"\  
"gopkg.in/op/go-logging.v1"\  
"github.com/BurntSushi/toml"\  
"github.com/delicb/gstring"\  
"github.com/etcinit/speedbump"\  
"github.com/go-redis/redis"\  
"github.com/graphql-go/graphql"\  
"github.com/graphql-go/graphql/gqlerrors"\  
"github.com/graphql-go/graphql/language/ast"\  
"github.com/mnmtanish/go-graphiql"\  
"github.com/satori/go.uuid"\  
"github.com/RichardKnop/machinery/v1"\  
"github.com/golang/freetype"\  
"github.com/subosito/twilio"\  
"github.com/lib/pq"\  
"golang.org/x/image/font"\  
"gopkg.in/olivere/elastic.v5"\  
"github.com/jtblin/go-ldap-client"\  
"gopkg.in/ldap.v2"\  
"gopkg.in/asn1-ber.v1"\  
"gopkg.in/h2non/filetype.v1"\  
"github.com/mattes/migrate"\  
"github.com/golang/lint/golint"\  
"github.com/domodwyer/mailyak"\  
"golang.org/x/crypto/bcrypt"\  
"github.com/icrowley/fake"\  
"github.com/streadway/amqp"\  
"github.com/golang/geo/s2"\  
"mvdan.cc/xurls"\  
"github.com/NaySoftware/go-fcm"\  
"github.com/Azure/azure-sdk-for-go/storage"  

