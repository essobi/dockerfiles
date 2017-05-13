FROM ruby:2.4
MAINTAINER thinkbot@outlook.de

ENV VERSION=0.9.4
RUN gem install bio-phyta --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["phyta-split"]
CMD ["--help"]
