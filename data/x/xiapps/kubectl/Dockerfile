FROM alpine:3.4  
MAINTAINER xiapps  
  
ARG VERSION=1.3.4  
ENV VERSION=${VERSION}  
ENV SHA1SUM_1_3_2 5c1ab430651074937e9f81c1726a77c67fa66356  
ENV SHA1SUM_1_3_3 9c8606757a00842fb25312f023db7baff50dac4b  
ENV SHA1SUM_1_3_4 4add464ea459f9f79b0b27be7b2600fb9ad395e2  
  
RUN echo "$(eval echo \$SHA1SUM_$(echo ${VERSION} | tr '.' '_'))
/usr/local/bin/kubectl"  
RUN apk add --update --no-cache openssl ca-certificates  
RUN update-ca-certificates  
RUN wget -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/v${VERSION}/bin/linux/amd64/kubectl  
RUN echo "$(eval echo \$SHA1SUM_$(echo ${VERSION} | tr '.' '_'))
/usr/local/bin/kubectl" | sha1sum -c -  
  
RUN chmod u+x /usr/local/bin/kubectl  
ADD docker-entrypoint.sh /  
  
RUN mkdir -p /var/kubectl  
  
WORKDIR /var/kubectl  
VOLUME ["/config-storage"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

