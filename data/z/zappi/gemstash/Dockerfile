FROM ruby:2.5.0-alpine  
  
# Install system dependencies  
RUN apk --update add \  
build-base \  
mariadb-dev \  
postgresql-dev \  
sqlite-dev \  
su-exec \  
tini && \  
gem update --system && \  
gem update bundler && \  
rm -rf /var/cache/apk/*  
  
# Create gemstash user  
ENV GEMSTASH_USER="gemstash"  
ENV GEMSTASH_HOME="/home/${GEMSTASH_USER}"  
RUN addgroup -g "9999" "${GEMSTASH_USER}" && \  
adduser -S -D -u "9999" -G "${GEMSTASH_USER}" "${GEMSTASH_USER}"  
  
# Install Gemstash  
RUN mkdir -p "${GEMSTASH_HOME}/app"  
WORKDIR "${GEMSTASH_HOME}/app"  
COPY "app/" "${GEMSTASH_HOME}/app"  
RUN bundle config disable_checksum_validation true && \  
bundle install --jobs 4 --retry 3  
  
VOLUME "${GEMSTASH_HOME}/data"  
  
EXPOSE 9292  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bundle", "exec", "gemstash", "start", "--no-daemonize"]  

