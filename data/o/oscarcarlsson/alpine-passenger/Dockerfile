FROM alpine:3.4  
  
ENV PASSENGER=passenger-5.0.28 \  
PATH="/passenger/bin:$PATH"  
  
ENV BUILD=0.0.1  
  
# Do it all in one step they said. It will be fun, they said.  
RUN apk update && apk add \--update ca-certificates curl gnupg && \  
curl -O "http://s3.amazonaws.com/phusion-
passenger/releases/$PASSENGER.tar.gz.asc" -O
"https://s3.amazonaws.com/phusion-passenger/releases/$PASSENGER.tar.gz" && \  
gpg \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys 0x2AC745A50A212A8C
&& \  
gpg \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys 0xCD70085E8C59158F
&& \  
gpg \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys 0xAE405F7869481265
&& \  
gpg \--verify $PASSENGER.tar.gz.asc $PASSENGER.tar.gz && \  
tar xzf "$PASSENGER.tar.gz" && \  
rm "$PASSENGER.tar.gz.asc" "$PASSENGER.tar.gz" && \  
# install build deps  
apk add ruby procps pcre libstdc++ glib-dev libc-dev openssl-dev make
libxml2-dev ruby-rake build-base linux-headers curl-dev pcre-dev ruby-dev
coreutils ruby-io-console libffi libffi-dev ruby-bundler && \  
apk add \--update-cache \--repository
'http://nl.alpinelinux.org/alpine/edge/testing' libexecinfo libexecinfo-dev &&
\  
# Install ffi while we have an build development  
# available. Version is from the Gemfile.lock in the actual  
# project, adjust to your needs!  
gem install ffi -v 1.9.10 \--no-rdoc \--no-ri && \  
# The same goes for eventmachine  
gem install eventmachine -v 1.0.9.1 \--no-rdoc \--no-ri && \  
# ...and json. And any other gem that requires native compilation.  
gem install json -v 1.8.3 \--no-rdoc \--no-ri && \  
# Start compiling phusion + nginx  
mv "$PASSENGER" /passenger && cd /passenger && \  
export EXTRA_PRE_CFLAGS='-O' EXTRA_PRE_CXXFLAGS='-O'
EXTRA_LDFLAGS='-lexecinfo' && \  
passenger-config install-standalone-runtime \--auto \--url-root=fake
\--connect-timeout=1 && \  
passenger-config build-native-support && \  
# save some space  
rm -rf /tmp/* /passenger/doc && \  
# remove build deps and apk cache  
apk del build-base coreutils curl-dev glib-dev gnupg libc-dev libexecinfo
libexecinfo-dev libffi libffi-dev libstdc++ libxml2-dev linux-headers make
openssl-dev pcre pcre-dev procps ruby-dev ruby-io-console && \  
rm -rf /var/cache/apk/* && \  
# validate install  
passenger-config validate-install \--auto && \  
mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
EXPOSE 3000  
  
ENTRYPOINT ["passenger", "start", "--no-install-runtime", "--no-compile-
runtime", "--no-download-binaries"]  

