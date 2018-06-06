FROM alpine:latest  
RUN apk add --no-cache curl  
RUN apk add --no-cache g++  
RUN apk add --no-cache make  
RUN apk add --no-cache linux-headers  
  
ARG DL_DIR="/tmp/capnproto"  
ARG DL_FORMAT="tar.gz"  
#ARG REPO="capnproto/capnproto"  
#ARG REF="master"  
#ARG URL="https://codeload.github.com/$REPO/$DL_FORMAT/$REF"  
ARG VERSION="0.6.1"  
ARG URL="https://capnproto.org/capnproto-c++-$VERSION.$DL_FORMAT"  
ARG MAKEFLAGS=""  
RUN echo "Downloading Cap'n Proto form $URL ..."; \  
mkdir -p "$DL_DIR" \  
&& curl "$URL" \  
| tar -xz -C "$DL_DIR"  
ARG CONFIGURE_FLAGS=""  
ARG CONFIGURE_CMD="./configure \$CONFIGURE_FLAGS"  
RUN echo "Configuring Cap'n Proto source ($CONFIGURE_CMD)..." \  
&& cd "$DL_DIR" && if [ `ls | wc -l` == 1 ]; then cd `ls`; fi \  
&& eval "$CONFIGURE_CMD"  
ARG BUILD_FLAGS="-j6"  
ARG BUILD_TARGET="check"  
ARG BUILD_CMD="make \$BUILD_FLAGS \$BUILD_TARGET"  
RUN echo "Building Cap'n Proto ($BUILD_CMD)..." \  
&& cd "$DL_DIR" && if [ `ls | wc -l` == 1 ]; then cd `ls`; fi \  
&& eval "$BUILD_CMD"  
ARG INSTALL_FLAGS=""  
ARG INSTALL_TARGET="install"  
ARG INSTALL_CMD="make \$INSTALL_FLAGS \$INSTALL_TARGET"  
RUN echo "Installing Cap'n Proto ($INSTALL_CMD)..." \  
&& cd "$DL_DIR" && if [ `ls | wc -l` == 1 ]; then cd `ls`; fi \  
&& eval "$INSTALL_CMD"  
RUN echo "Cleaning up after Cap'n Proto installation..." \  
&& rm -rf "$DL_DIR"  

