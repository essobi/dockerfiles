FROM alpine:3.4  
MAINTAINER Mike Simons <dockerhub@mikesimons.co.uk>  
  
ENV VERSION 0.15.0  
ENV URL http://releases.hashicorp.com/consul-template/${VERSION}/consul-
template_${VERSION}_linux_amd64.zip  
ENV SHA256 b7561158d2074c3c68ff62ae6fc1eafe8db250894043382fb31f0c78150c513a  
  
RUN apk --no-cache add curl && \  
cd /tmp && \  
curl -L $URL -o consul-template.zip && \  
echo "${SHA256} consul-template.zip" | sha256sum -c && \  
cd /usr/local/bin && \  
unzip /tmp/consul-template.zip && \  
chmod +x /usr/local/bin/consul-template && \  
rm -rf /tmp/consul-template.zip  
  
ENTRYPOINT ["/usr/local/bin/consul-template"]  

