FROM ruby:2.2.7-alpine  
  
VOLUME /massikone/data  
EXPOSE 3000  
COPY . /massikone  
WORKDIR /massikone  
RUN apk update \  
&& apk add \  
imagemagick \  
mariadb-client-libs \  
mariadb-libs \  
postgresql-libs \  
sqlite \  
sqlite-libs \  
&& apk add --virtual builddeps \  
build-base \  
mariadb-dev \  
postgresql-dev \  
sqlite-dev \  
&& bundle install --no-cache \  
&& apk del builddeps \  
&& rm -rf /var/cache/apk \  
&& true  
RUN adduser -D massikone  
RUN chown -R massikone:massikone .  
USER massikone  
CMD puma -p 3000  

