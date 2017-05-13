FROM alpine:edge

ENV VER=6.1.8280
ENV GID=1000 UID=1000
RUN apk -U add \
    ffmpeg \
    openjdk8-jre \
    tini \
    bash \
 && rm -f /var/cache/apk/*

WORKDIR /madsonic
RUN wget -qO- http://madsonic.org/download/6.1/20160505_madsonic-6.1.8280-standalone.tar.gz | tar zxf -

COPY run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh

EXPOSE 4040
VOLUME /data /musics /playlists /podcasts
LABEL description "Open source media streamer" \
      subsonisc "Madsonic v$VER"
CMD ["tini","--","run.sh"]
