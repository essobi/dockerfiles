FROM zooniverse/ruby:2.1

WORKDIR /src/

RUN apt-get update && apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

ADD ./ /src/

RUN mkdir -p data

RUN cd lib && bundle install
