FROM anigeo/awscli  
MAINTAINER Sébastien De Saint Florent <sdesaintflorent@tribalnova.com>  
  
RUN apk add --update --no-cache jq  
ADD query.sh /usr/local/bin/dynamodb-query.sh  
  
ENTRYPOINT [ "dynamodb-query.sh" ]

