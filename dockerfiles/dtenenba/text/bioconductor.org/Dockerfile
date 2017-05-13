FROM ubuntu:14.04
MAINTAINER dtenenba@fredhutch.org

EXPOSE 3000
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && apt-get dist-upgrade -y && apt-get install -y \
    curl g++ git libsqlite3-dev make patch python rsync subversion build-essential zlib1g-dev libssl-dev libreadline-dev libyaml-dev libxml2-dev libxslt-dev libffi-dev postgresql-server-dev-all

# make ruby 2.0 the default
#RUN for i in `ls /usr/bin/*2.0`; do  ln -sf $i `echo $i | tr -d 2.0`  ; done
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv

RUN echo 'eval "$(rbenv init -)"' >> ~/.bash_profile

RUN git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build

RUN ./root/.rbenv/plugins/ruby-build/install.sh

ENV PATH /root/.rbenv/bin:/root/.rbenv/shims:$PATH
ENV CONFIGURE_OPTS --disable-install-doc

RUN rbenv install -v 2.2.1
RUN rbenv global 2.2.1

RUN curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install --upgrade google-api-python-client
RUN pip install python-dateutil

# RUN pip install apiclient? # for dashboard stuff
RUN cd /tmp && \
    curl -O https://raw.githubusercontent.com/Bioconductor/bioconductor.org/master/Gemfile && \
    curl -O https://raw.githubusercontent.com/Bioconductor/bioconductor.org/master/Gemfile.lock && \
    echo "gem: --no-document" > /etc/gemrc && \
    gem install bundler && \
    bundle config build.pg --with-pg-lib=/usr/lib/postgresql/ --with-pg-include=/usr/include/postgresql/ && \
    bundle install

RUN rbenv rehash

VOLUME /bioconductor.org

WORKDIR /bioconductor.org

CMD rake && adsf -r output && sleep infinity
