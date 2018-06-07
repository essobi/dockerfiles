FROM patrinhani/gcloud  
  
# Begin - Go lang Configuration  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
build-essential ca-certificates git mercurial bzr  
RUN mkdir /goroot && curl https://storage.googleapis.com/golang/go1.4.2.linux-
amd64.tar.gz | tar xvzf - -C /goroot --strip-components=1  
RUN mkdir -p /gopath/src/app  
  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
ADD go-build /bin/go-build  
ADD go-run /bin/go-run  
  
ONBUILD ADD . /gopath/src/app/  
ONBUILD RUN /bin/go-build  
  
# End - Go lang Configuration  
# Begin - HBase Client  
ENV GOOGLE_APPLICATION_CREDENTIALS=/hbase/conf/key.json  
  
WORKDIR /  
  
RUN mkdir hbase  
RUN curl http://storage.googleapis.com/cloud-bigtable/hbase-
dist/hbase-1.0.1/hbase-1.0.1-bin.tar.gz \  
| tar -zxC hbase --strip-components=1  
  
RUN mkdir -p hbase/lib/bigtable  
RUN curl -0 https://storage.googleapis.com/cloud-bigtable/jars/bigtable-
hbase/bigtable-hbase-1.0-0.1.9-shaded.jar \  
-o /hbase/lib/bigtable/bigtable-hbase-0.1.9.jar  
RUN curl -0 http://central.maven.org/maven2/org/mortbay/jetty/alpn/alpn-
boot/7.1.3.v20150130/alpn-boot-7.1.3.v20150130.jar \  
-o /hbase/lib/bigtable/alpn-boot-7.1.3.v20150130.jar  
  
RUN echo "export HBASE_CLASSPATH=/hbase/lib/bigtable/bigtable-hbase-0.1.9.jar"
>>/hbase/conf/hbase-env.sh && \  
echo "export HBASE_OPTS=\"${HBASE_OPTS} -Xms1024m -Xmx2048m
-Xbootclasspath/p:/hbase/lib/bigtable/alpn-boot-7.1.3.v20150130.jar\""
>>/hbase/conf/hbase-env.sh  
  
ADD hbase/conf/. /hbase/conf  
  
ADD gopath/src/. /gopath/src  
  
ENV PATH /hbase/bin:$PATH  
  
# End - HBase Client  
# Env setup  
WORKDIR /gopath/src  
  
RUN go get golang.org/x/net/context  
RUN go get golang.org/x/oauth2/google  
RUN go get google.golang.org/cloud  
RUN go get google.golang.org/cloud/bigtable  
  
RUN go install ciandt.golang.org/libs/gbigtable  
RUN go install ciandt.golang.org/libs/ioutil  
  
WORKDIR /gopath/src/app  
  
EXPOSE 8080

