# BOOSTER-WEB docker file, with a running Galaxy instance  
# Containing all required phylogenetic tools  
# https://hub.docker.com/r/evolbioinfo/booster-web  
# base image: evolbioinfo/ngphylogeny-galaxy  
FROM evolbioinfo/ngphylogeny-galaxy  
  
# File Author / Maintainer  
MAINTAINER Frederic Lemoine <frederic.lemoine@pasteur.fr>  
  
COPY . /gopath/src/github.com/evolbioinfo/booster-web  
COPY docker/booster-web.toml /home/booster/booster-web.toml  
  
# Build booster-web  
ENV PATH=/usr/local/go/bin:/gopath/bin/:$PATH  
ENV GOPATH=/gopath  
  
RUN wget --no-check-certificate -O /usr/local/go1.9.2.linux-amd64.tar.gz
https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzf /usr/local/go1.9.2.linux-amd64.tar.gz \  
&& rm -f /usr/local/go1.9.2.linux-amd64.tar.gz \  
&& mkdir -p /gopath/ \  
&& go get -u github.com/golang/dep/cmd/dep \  
&& go get github.com/jteeuwen/go-bindata/... \  
&& go get github.com/elazarl/go-bindata-assetfs/... \  
&& cd /gopath/src/github.com/evolbioinfo/booster-web \  
&& dep ensure \  
&& go-bindata-assetfs -pkg static webapp/static/... \  
&& mv bindata.go static \  
&& go-bindata -o bindata_templates.go -pkg templates webapp/templates/... \  
&& mv bindata_templates.go templates \  
&& go build -o booster-web -ldflags "-X github.com/evolbioinfo/booster-
web/cmd.Version=v1.8" github.com/evolbioinfo/booster-web \  
&& mv booster-web /home/booster/booster-web \  
&& rm -rf /gopath /usr/local/go  
  
ENV
GALAXY_CONFIG_TOOL_CONFIG_FILE=config/tool_conf.xml.sample,config/shed_tool_conf.xml.sample,/local_tools/tool_conf.xml  
ENV GALAXY_DOCKER_ENABLED=True  
EXPOSE :80  
EXPOSE :21  
EXPOSE :22  
EXPOSE :8800  
EXPOSE :8000  
CMD ["sh", "-c", "/usr/bin/startup & galaxy-wait && /home/booster/booster-web
--config /home/booster/booster-web.toml"]  

