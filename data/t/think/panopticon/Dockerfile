FROM ubuntu:16.04  
  
MAINTAINER think@hotmail.de  
  
ENV RUST_VERSION=1.12.0  
# TODO: uninstall dev packages  
RUN apt-get update \  
&& apt-get install -y \  
qt5-default qtdeclarative5-dev \  
libqt5svg5-dev \  
qml-module-qtquick-controls qml-module-qttest \  
qml-module-qtquick2 qml-module-qtquick-layouts \  
qml-module-qtgraphicaleffects qml-module-qtqml-models2 \  
qml-module-qtquick-dialogs \  
qtbase5-private-dev pkg-config \  
git build-essential cmake libqwt-qt5-dev curl tar gzip \  
&& curl -sO https://static.rust-
lang.org/dist/rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz \  
&& tar -xzf rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz \  
&& rm rust-*.tar.gz \  
&& ./rust-$RUST_VERSION-x86_64-unknown-linux-gnu/install.sh --without=rust-
docs \  
&& git clone https://github.com/das-labor/panopticon.git \  
&& cd panopticon \  
&& cargo build --release \  
&& apt-get auto-remove -y curl  
  
CMD ["qtpanopticon"]  

