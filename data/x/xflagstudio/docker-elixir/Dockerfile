FROM amazonlinux:1  
  
ENV ELIXIR_VERSION "1.6.5-otp-20"  
ENV ERLANG_VERSION "20.3"  
ENV ASDF_VERSION "v0.4.1"  
ENV ASDF_DIR /opt/asdf  
ENV PATH "/opt/asdf/bin:/opt/asdf/shims:$PATH"  
  
RUN yum groupinstall -y 'Development Tools' && \  
yum install -y automake autoconf readline-devel openssl-devel ncurses-devel
unixODBC-devel libyaml-devel libxslt-devel libffi-devel libtool ca-
certificates git unzip which perl python27-pip bash && \  
curl --silent \--location https://rpm.nodesource.com/setup_8.x | bash - && \  
yum install -y nodejs && \  
git clone https://github.com/asdf-vm/asdf.git /opt/asdf --branch $ASDF_VERSION
&& \  
asdf plugin-add erlang https://github.com/asdf-vm/asdf-erlang.git && \  
asdf install erlang $ERLANG_VERSION && \  
asdf global erlang $ERLANG_VERSION && \  
asdf plugin-add elixir https://github.com/asdf-vm/asdf-elixir.git && \  
asdf install elixir $ELIXIR_VERSION && \  
asdf global elixir $ELIXIR_VERSION && \  
yes | mix local.hex --force && \  
yes | mix local.rebar --force && \  
pip install --no-cache-dir python-dateutil && \  
git clone https://github.com/s3tools/s3cmd.git /opt/s3cmd && \  
ln -s /opt/s3cmd/s3cmd /usr/bin/s3cmd  
  

