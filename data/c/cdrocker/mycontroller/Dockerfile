FROM alpine:latest  
ENV VERSION=1.2.0  
ENV MYCONTROLLER_URL="https://github.com/mycontroller-
org/mycontroller/releases/download/${VERSION}.Final/mycontroller-dist-
standalone-${VERSION}.Final-bundle.tar.gz"  
LABEL \  
org.label-schema.maintainer="me codar nl" \  
org.label-schema.name="mycontroller" \  
org.label-schema.description="Mycontroller running on Alpine Linux" \  
org.label-schema.version="${VERSION}" \  
org.label-schema.vcs-url="https://github.com/githubcdr/docker-mycontroller" \  
org.label-schema.schema-version="1.0"  
  
# pin to /tmp  
WORKDIR /tmp  
  
# dependencies  
RUN apk add --update --no-cache s6 ca-certificates openjdk8-jre-base wget  
  
# install  
RUN wget $MYCONTROLLER_URL -O mycontroller.tar.gz \  
&& tar zxf mycontroller.tar.gz -C /usr/local \  
&& rm -f /tmp/*  
  
# add files  
COPY files/root/ /  
  
# fixes  
RUN chmod +x /service/*/run  
  
# expose mqtt and web  
EXPOSE 1883/tcp 8443/tcp  
  
# launch s6  
ENTRYPOINT ["/bin/s6-svscan","/service"]  

