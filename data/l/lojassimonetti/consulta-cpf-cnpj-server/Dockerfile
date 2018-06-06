FROM golang:1.5.3  
ENV GOPATH /usr/local/consulta-cpf-cnpj-server  
  
WORKDIR /usr/local/consulta-cpf-cnpj-server  
  
ADD . /usr/local/consulta-cpf-cnpj-server  
  
RUN apt-get update \  
&& apt-get install -y pkg-config libcurl4-openssl-dev  
  
RUN cd /usr/local/consulta-cpf-cnpj-server \  
&& go get github.com/PuerkitoBio/goquery \  
&& go get github.com/andelf/go-curl \  
&& go get github.com/go-martini/martini \  
&& go get github.com/ryanuber/go-filecache \  
&& go get github.com/andelf/iconv-go  
  
RUN go build  
  
EXPOSE 3000  
  
CMD ["/usr/local/consulta-cpf-cnpj-server/consulta-cpf-cnpj-server"]

