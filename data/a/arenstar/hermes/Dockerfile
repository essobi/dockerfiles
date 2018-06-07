FROM alpine:3.3  
RUN apk add --no-cache openssl-dev libspf2-dev sqlite-dev git make g++
automake autoconf gettext-dev  
  
ENV HERMES_VERSION 1.9  
RUN cd /tmp && git clone https://github.com/jjguti/hermes.git  
  
WORKDIR /tmp/hermes  
  
RUN /bin/sh ./bootstrap  
  
RUN ./configure \  
\--enable-spf \  
\--enable-openssl  
  
RUN make && make install  
  
WORKDIR /  
  
RUN mkdir -p /etc/hermes /var/hermes && chown nobody:nogroup -R /etc/hermes
/var/hermes  
  
COPY hermesrc /etc/hermes/hermesrc  
  
EXPOSE 25  
CMD ["hermes","/etc/hermes/hermesrc"]  

