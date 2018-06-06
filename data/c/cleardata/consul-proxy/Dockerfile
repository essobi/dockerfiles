FROM golang:1.4  
RUN apt-get -y update && apt-get install -y --no-install-recommends haproxy
nginx git && rm -rf /var/lib/apt/lists/*  
RUN cd /tmp && git clone https://github.com/hashicorp/consul-template.git &&
cd consul-template && make && cp bin/consul-template /go/bin/consul-template
&& cd /tmp && rm -rf consul-template  

