FROM nginx  
  
MAINTAINER Joakim Ahrlin "joakim.ahrlin@gmail.com"  
#update stuffs  
RUN apt-get update && apt-get install -y \  
git \  
curl \  
mercurial  
  
RUN mkdir /goroot && curl https://storage.googleapis.com/golang/go1.6.linux-
amd64.tar.gz | tar xvzf - -C /goroot --strip-components=1  
  
RUN mkdir /gopath  
  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
RUN go get -v github.com/spf13/hugo  
RUN go install github.com/spf13/hugo  
  
ADD site-source /site-source  
RUN cd /site-source && \  
hugo  
  
RUN cp -R /site-source/public /app/  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
#ADD sites-enabled/ /etc/nginx/sites-enabled/  
#ADD app/ /app/  
EXPOSE 80  
CMD ["/usr/sbin/nginx"]  

