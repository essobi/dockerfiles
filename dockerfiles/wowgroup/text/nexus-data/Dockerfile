FROM busybox
MAINTAINER WOW! Group Development

RUN adduser -h /sonatype-work -u 200 -D nexus

VOLUME /sonatype-work
WORKDIR /sonatype-work
USER nexus
