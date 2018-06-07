## Dockerfile for a haskell environment, with lts stackage and all packages
preinstalled  
FROM sideeffffect/haskell-stackage:2  
MAINTAINER Ondra Pelech <ondra.pelech@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN cabal update  
  
RUN which ghc && \  
ghc --version && \  
which cabal && \  
cabal --version && \  
ghc-pkg list  
  
RUN cabal install text \  
warp \  
attoparsec \  
lens \  
aeson \  
cabal-install \  
persistent \  
conduit \  
Cabal \  
network \  
wai-extra \  
parsec \  
HTTP \  
yesod-core \  
blaze-html \  
hspec \  
conduit-extra \  
yesod-auth \  
xml-conduit \  
zlib \  
blaze-markup \  
hlint \  
yesod \  
pandoc \  
tagged \  
persistent-template \  
http-client \  
QuickCheck \  
shake \  
system-filepath \  
streaming-commons \  
ghc-mod \  
contravariant \  
classy-prelude \  
resourcet \  
highlighting-kate \  
http-conduit \  
hscolour \  
texmath \  
wai-app-static \  
yesod-bin \  
hashable \  
semigroupoids \  
shelly \  
JuicyPixels \  
profunctors \  
tls \  
yesod-form \  
yaml \  
scientific \  
snap-server \  
MonadRandom \  
optparse-applicative \  
transformers-compat \  
authenticate \  
transformers \  
semigroups \  
vector \  
reflection \  
either \  
monad-control \  
persistent-sqlite \  
shakespeare \  
case-insensitive \  
haskell-src-exts \  
iproute \  
binary \  
comonad \  
system-fileio \  
hakyll \  
file-embed \  
primitive \  
free \  
persistent-postgresql \  
unordered-containers \  
blaze-builder \  
hspec-discover \  
syb \  
network-uri \  
simple-sendfile \  
cereal \  
hspec-core \  
old-time \  
basic-prelude \  
mtl \  
snap \  
adjunctions \  
fast-logger \  
pointed \  
cookie \  
OpenGLRaw \  
async \  
esqueleto \  
cpphs \  
snap-core \  
bifunctors \  
wai \  
hoogle \  
mime-mail \  
utf8-string  
  
RUN which ghc && \  
ghc --version && \  
which cabal && \  
cabal --version && \  
ghc-pkg list  
  
## run ghci by default unless a command is specified  
CMD ["ghci"]  
  

