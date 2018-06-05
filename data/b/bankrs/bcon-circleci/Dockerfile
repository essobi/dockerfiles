FROM golang:1.10.2-stretch  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
apt-utils ca-certificates curl make git ssh apt-transport-https software-
properties-common python-wheel python-pip python-setuptools gnupg  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian $(lsb_release -cs) stable"  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
docker-ce=18.03.1~ce-0~debian  
RUN curl -fsSL https://deb.nodesource.com/setup_10.x | bash -;
DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs && npm install -g
--no-progress junit-merge && npm cache clean --force  
RUN rm -rf /var/lib/apt/lists/*  
RUN pip install --upgrade awscli  
RUN curl -fsSL
"https://github.com/docker/compose/releases/download/1.21.2/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
RUN go get -u github.com/golang/lint/golint  
RUN go get -u honnef.co/go/tools/cmd/megacheck  
RUN go get -u github.com/gordonklaus/ineffassign  
RUN go get -u github.com/remyoudompheng/go-misc/deadcode  
RUN go get -u github.com/client9/misspell/cmd/misspell  
RUN go get -u github.com/mdempsky/unconvert  
RUN go get -u github.com/jgautheron/goconst  
  
CMD ["/bin/bash"]  

