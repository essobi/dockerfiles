FROM ubuntu:16.04  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y build-
essential git ruby ruby-dev wget jq curl  
  
RUN gem install cf-uaac  
  
ADD https://github.com/pivotalservices/cf-mgmt/releases/download/v0.0.85/cf-
mgmt-linux /usr/bin/cf-mgmt  
RUN chmod +x /usr/bin/cf-mgmt  
  
ADD https://github.com/pivotalservices/cf-mgmt/releases/download/v0.0.85/cf-
mgmt-config-linux /usr/bin/cf-mgmt-config  
RUN chmod +x /usr/bin/cf-mgmt-config  
  
ADD
https://github.com/s-matyukevich/yaml2json/releases/download/0.0.1/yaml2json
/usr/bin/yaml2json  
RUN chmod +x /usr/bin/yaml2json  
  
ADD https://github.com/pivotal-cf/om/releases/download/0.25.0/om-linux
/usr/local/bin/om  
RUN chmod +x /usr/local/bin/om  
  
RUN wget https://github.com/cloudfoundry-incubator/credhub-
cli/releases/download/1.7.0/credhub-linux-1.7.0.tgz && \  
tar -xvf credhub-linux-1.7.0.tgz && \  
mv credhub /usr/local/bin && \  
rm credhub-linux*  
  
RUN curl -sL
"https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar
-zx && mv cf /usr/local/bin/  

