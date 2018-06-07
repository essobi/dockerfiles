FROM gliderlabs/alpine:latest  
  
ENV PACKAGES build-base git libcrypto1.0 py-pip python ruby ruby-bundler ruby-
dev ruby-json ruby-libs ruby-io-console ruby-bigdecimal tini  
ENV PACKAGES_CLEANUP build-base git py-pip py-setuptools  
  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
  
COPY Gemfile /  
  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" && \  
chmod 755 "$GEM_HOME" "$BUNDLE_BIN" && \  
echo "http://dl-1.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "http://dl-2.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "http://dl-3.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "http://dl-5.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk --update --no-cache add ${PACKAGES} && \  
pip install awscli && \  
echo 'gem: --no-rdoc --no-ri' >> "${HOME}/.gemrc" && \  
bundle install && \  
apk --purge -v del ${PACKAGES_CLEANUP} && \  
rm -vfr /usr/share/ri && \  
rm /var/cache/apk/* && \  
mkdir -p /messages/sns && \  
chown -R nobody:nobody /messages/sns/  
  
VOLUME /messages/sns  
  
EXPOSE 9292  
ENTRYPOINT ["tini", "--"]  
  
USER nobody  
  
# Note: We use thin, because webrick attempts to do a reverse dns lookup on
every request  
# which slows the service down big time. There is a setting to override this,
but sinatra  
# does not allow server specific settings to be passed down.  
CMD fake_sns --bind 0.0.0.0 --database=/messages/sns/database.yml --port 9292
--server thin  

