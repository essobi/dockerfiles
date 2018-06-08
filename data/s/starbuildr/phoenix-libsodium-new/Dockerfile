FROM starbuildr/phoenix-new:1.0.8  
MAINTAINER Vyacheslav Voronchuk <voronchuk@gmail.com>  
  
RUN apt-get update && apt-get install -y libtool  
RUN apt-get install -y autoconf  
RUN apt-get install -y letsencrypt  
RUN git clone -b '1.0.11' \--single-branch --depth 1
https://github.com/jedisct1/libsodium  
WORKDIR libsodium  
RUN ./autogen.sh  
RUN ./configure && make check  
RUN make install  
  
WORKDIR /var/app  
COPY ./config /var/app/config  
COPY ./certificates /var/app/certificates  
COPY ./mix.exs /var/app/mix.exs  
COPY ./mix.lock /var/app/mix.lock  
  
RUN mix local.hex --force \  
&& mix deps.get --only prod \  
&& mix deps.compile  
  
# SSL setting  
RUN openssl dhparam -out /var/app/config/dhparam.pem 2048  
  
# Install Node Deps  
COPY ./assets/brunch-config.js /var/app/assets/brunch-config.js  
COPY ./assets/package.json /var/app/assets/package.json  
RUN cd assets && npm install  
  
ENTRYPOINT ["mix", "phx.new"]  
CMD ["/var/app"]  

