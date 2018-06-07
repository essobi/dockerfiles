FROM easymile/elixir:1.6.4  
  
MAINTAINER frederic.cabestre [at] easymile.com  
  
RUN addgroup builder -g 1000 && \  
adduser builder -u 1000 -s /bin/ash -SDG builder && \  
apk add --update sudo && \  
echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
USER builder  
WORKDIR /home/builder  
  
RUN sudo apk add --no-cache --update \  
jq=1.5-r4 \  
protobuf=3.4.1-r1 \  
# Required to build `ShellCheck`  
ghc=8.0.2-r6 \  
cabal=1.24.0.2-r1 \  
libffi=3.2.1-r4 \  
&& \  
# Build ShellCheck  
cabal update && \  
cabal install ShellCheck-0.4.6 && \  
sudo cp .cabal/bin/shellcheck /usr/bin/shellcheck && \  
rm -rf .cabal/bin/shellcheck && \  
  
sudo chown builder. -R /usr/local/asdf && \  
sudo apk del --no-cache alpine-sdk diffutils elfutils-dev ncurses opam ocaml
cabal ghc && \  
sudo rm -rf /var/cache/apk/* && \  
asdf global erlang "$ASDF_ERLANG_VERSION" && \  
asdf global elixir "$ELIXIR_VERSION" && \  
mix local.hex --force && \  
mix local.rebar --force  

