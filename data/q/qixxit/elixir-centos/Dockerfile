FROM centos:7  
MAINTAINER Daniel Temme <daniel@qixxit.de>  
  
ENV ERLANG_VERSION=20.2  
ENV ELIXIR_VERSION=1.6.1  
ENV RUBY_VERSION=2.4.3  
ENV ERL_AFLAGS="-kernel shell_history enabled"  
ARG DISABLED_APPS='megaco wx debugger jinterface orber reltool observer et'  
ARG ERLANG_TAG=OTP-${ERLANG_VERSION}  
ARG ELIXIR_TAG=v${ELIXIR_VERSION}  
  
LABEL erlang_version=$ERLANG_VERSION erlang_disabled_apps=$DISABLED_APPS
elixir_version=$ELIXIR_VERSION ruby_version=$RUBY_VERSION  
  
RUN yum update -y && yum clean all  
RUN yum reinstall -y glibc-common && yum clean all  
RUN yum install -y centos-release-scl && yum clean all  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
  
RUN locale  
  
RUN yum -y install \  
git \  
ncurses-devel \  
install \  
gcc \  
gcc-c++ \  
make \  
cmake \  
openssl-devel \  
autoconf \  
zip \  
bzip2 \  
readline-devel \  
&& yum clean all  
  
# Install Ruby (system ruby is too old)  
RUN set -xe \  
cd /tmp \  
&& git clone \--depth=1 https://github.com/rbenv/ruby-build.git \  
&& PREFIX=/usr/local ./ruby-build/install.sh \  
&& ruby-build $RUBY_VERSION /root/.local/ruby  
  
ENV PATH=/root/.local/ruby/bin/:$PATH  
  
# Install Erlang  
RUN set -xe \  
cd /tmp \  
&& git clone \--branch $ERLANG_TAG \--depth=1 --single-branch
https://github.com/erlang/otp.git \  
&& cd otp \  
&& echo "ERLANG_BUILD=$(git rev-parse HEAD)" >> /info.txt \  
&& echo "ERLANG_VERSION=$(cat OTP_VERSION)" >> /info.txt \  
&& for lib in ${DISABLED_APPS} ; do touch lib/${lib}/SKIP ; done \  
&& ./otp_build autoconf \  
&& ./configure \  
\--enable-smp-support \  
\--enable-m64-build \  
\--disable-native-libs \  
\--enable-sctp \  
\--enable-threads \  
\--enable-kernel-poll \  
\--disable-hipe \  
&& make -j$(nproc) \  
&& make install \  
&& find /usr/local -name examples | xargs rm -rf \  
&& ls -d /usr/local/lib/erlang/lib/*/src | xargs rm -rf \  
&& rm -rf \  
/otp/* \  
/tmp/*  
  
# Install Elixir  
RUN cd /tmp \  
&& git clone https://github.com/elixir-lang/elixir.git \  
&& cd elixir  
  
RUN git clone \--branch $ELIXIR_TAG \--depth=1 --single-branch
https://github.com/elixir-lang/elixir.git \  
&& cd elixir \  
&& echo "ELIXIR_BUILD=$(git rev-parse HEAD)" >> /info.txt \  
&& echo "ELIXIR_VERSION=$(cat VERSION)" >> /info.txt \  
&& make -j$(nproc) compile \  
&& rm -rf .git \  
&& make install \  
&& cd / \  
&& rm -rf \  
/tmp/*  
  
RUN echo cat /info.txt  
  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
RUN cd /tmp \  
&& git clone https://github.com/jeremyjh/dialyxir.git \  
&& cd dialyxir \  
&& MIX_ENV=prod mix do compile, archive.build \  
&& MIX_ENV=prod mix archive.install --force \  
&& cd / \  
&& MIX_ENV=test mix dialyzer --plt \  
&& rm -rf \  
/tmp/*  
  
RUN gem install pronto-credo --no-ri --no-rdoc -v 0.0.7  
RUN gem install pronto-dialyzer --no-ri --no-rdoc -v 0.3.0  
  
RUN yum -y install epel-release && yum clean all  
RUN yum -y install python-pip && yum clean all  
  
RUN pip install --upgrade pip && pip install --upgrade --user awscli  
ENV PATH=/root/.local/bin/:$PATH  
  
CMD ["/bin/sh"]  

