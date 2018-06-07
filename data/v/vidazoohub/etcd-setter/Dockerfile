# using alpine because it's the smallest i can use  
FROM alpine:3.3  
# whoami  
MAINTAINER naor livne <naorlivne@gmail.com>  
  
#update the index so i can actully use it for something & install curl  
RUN apk update && apk add curl  
  
# adding the codebase  
RUN mkdir /etcd-setter  
COPY / /etcd-setter/  
RUN chmod +x /etcd-setter/etcd_set_ttl.sh  
  
#changing rundir  
WORKDIR /etcd-setter  
  
# and running it  
CMD sh /etcd-setter/etcd_set_ttl.sh  
  

