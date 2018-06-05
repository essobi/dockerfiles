FROM alpine:3.4  
MAINTAINER Atsushi Nagase<a@ngs.io>  
  
RUN apk --no-cache add libreoffice curl go poppler-utils  
  
WORKDIR /var/tmp  
  
RUN curl -sLo noto.zip https://noto-
website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip && \  
unzip noto.zip && \  
mkdir -p /usr/share/fonts/Type1 && \  
mv *.otf /usr/share/fonts/Type1 && \  
rm -f *  
  
RUN mkdir /go  
ENV GOPATH /go  
WORKDIR /go  
  
ADD vendor src  
ADD convserver.go .  
  
RUN go build -o /usr/bin/convserver convserver.go  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/convserver"]  
  

