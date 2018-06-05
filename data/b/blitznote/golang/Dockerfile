FROM blitznote/golang:latest as gotools  
  
RUN go get \  
github.com/gordonklaus/ineffassign \  
github.com/golang/lint/golint \  
github.com/golang/dep/cmd/dep \  
&& go get -d github.com/Masterminds/glide \  
&& (cd $GOPATH/src/github.com/Masterminds/glide/ && make build && mv glide
$GOPATH/bin/) \  
&& find $GOPATH/bin -type f -executable \  
| xargs --max-lines=1 \--max-procs=$(nproc) --no-run-if-empty upx --best -q  
  
FROM blitznote/debase:16.04  
# prereqs used by and with some Golang packages  
RUN apt-get -q update \  
&& apt-get -y --no-install-recommends install \  
g++ \  
gcc \  
binutils \  
libc6-dev \  
make \  
pkg-config \  
git \  
openssh-client \  
&& (cd /usr/share/doc/git/contrib/diff-highlight && make) \  
&& cp -a /usr/share/doc/git/contrib/diff-highlight/diff-highlight /usr/bin/ \  
&& printf "[color]\n\tdiff = auto\n\tstatus = auto\n\tbranch =
auto\n[gpg]\n\tprogram = gpg2\n[diff]\n\tcompactionHeuristic =
true\n[pager]\n\tlog = /usr/bin/diff-highlight | less -r\n\tshow =
/usr/bin/diff-highlight | less -r\n\tdiff = /usr/bin/diff-highlight | less
-r\n[interactive]\n\tdiffFilter = /usr/bin/diff-highlight\n" >/root/.gitconfig
\  
&& rm -rf /usr/share/{doc,man,info} &>/dev/null \  
&& find /usr/share/locale/ -maxdepth 1 -mindepth 1 -type d -exec rm -r '{}' \;
\  
&& find /var -name '*-old' -type f -delete \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir -p ~/.ssh && chmod 0700 ~/.ssh \  
&& ssh-keyscan \  
hub.blitznote.com \  
github.com \  
bitbucket.org \  
git.sv.gnu.org \  
|& grep -v -F '#' >>~/.ssh/known_hosts  
  
# tools which don't need to be built using Golang  
RUN cd /tmp \  
&& curl --silent --show-error --fail --location --remote-name-all \  
$(curl --silent --show-error --fail --location --header 'Accept:
application/json' \--compressed \  
"https://api.github.com/repos/google/protobuf/releases" \  
| jq -r '.[].assets[] | select((.browser_download_url|endswith(".zip")) and
(.browser_download_url|contains("/protoc-"))) | .browser_download_url' \  
| grep -m 1 -F linux-x86_64) \  
&& unzip protoc-*.zip bin/protoc -d /usr/ \  
&& chmod a+x /usr/bin/protoc \  
&& /usr/bin/protoc --version \  
&& rm protoc-*.zip \  
&& curl --silent --show-error --fail --location --header "Accept:
application/tar+xz, application/x-xz, application/octet-stream" \  
$(curl --silent --show-error --fail --location --header 'Accept:
application/json' \  
"https://api.github.com/repos/upx/upx/releases/latest" \  
| jq -r '.assets[] | select(.name | contains("linux")) | select(.name |
contains("'$(dpkg --print-architecture)'")) | select(.browser_download_url |
contains(".tar.xz")) | .browser_download_url') \  
| tar --no-same-owner --strip-components=1 \--wildcards -C /usr/bin/ -xJ
"*/upx" \  
&& /usr/bin/upx --version  
  
ENV GOLANG_VERSION="1.10.2" \  
GOPATH="/go" \  
GOROOT="/opt/go" \  
PATH="$GOPATH/bin:/opt/go/bin:$PATH"  
  
LABEL org.label-schema.vendor="Blitznote" \  
org.label-schema.name="Golang" \  
org.label-schema.version="${GOLANG_VERSION}" \  
org.label-schema.vcs-ref="" \  
org.label-schema.vcs-type="git" \  
org.label-schema.vcs-url="https://github.com/Blitznote/golang"  
# install the pre-compiled vanilla Golang to /opt/go  
RUN mkdir -p "${GOPATH}" "${GOROOT}" \  
&& chmod 1777 "${GOPATH}" \  
&& curl --fail --location --silent --show-error -o - \  
"https://dl.google.com/go/go${GOLANG_VERSION}.linux-$(dpkg --print-
architecture).tar.gz" \  
| tar --no-same-owner --strip-components=1 -xz -C "${GOROOT}"/ \  
&& go version  
  
COPY --from=gotools --chown=0:0 /go/bin/* /usr/local/bin/  
  
WORKDIR $GOPATH  

