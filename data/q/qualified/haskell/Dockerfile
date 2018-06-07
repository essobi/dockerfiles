FROM buildpack-deps:xenial  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
ENV RESOLVER=lts-6.24 \  
GHC_VER=7.10.3 \  
CABAL_VER=1.22 \  
HAPPY_VER=1.19.5  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
software-properties-common \  
python-software-properties \  
; \  
add-apt-repository ppa:hvr/ghc; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
ghc-${GHC_VER} \  
cabal-install-${CABAL_VER} \  
happy-${HAPPY_VER} \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
PATH=/home/codewarrior/.cabal/bin:/opt/ghc/${GHC_VER}/bin:/opt/cabal/${CABAL_VER}/bin:/opt/happy/${HAPPY_VER}/bin:$PATH  
  
RUN set -ex; \  
mkdir -p $HOME/.cabal/bin; \  
echo "remote-repo: stackage_${RESOLVER}:http://www.stackage.org/${RESOLVER}"
>> $HOME/.cabal/config; \  
echo "remote-repo-cache: ${HOME}/.cabal/packages" >> $HOME/.cabal/config;  
  
RUN set -ex; \  
cabal update; \  
cabal install \  
# > A Testing Framework for Haskell http://hspec.github.io/  
hspec \  
# > Manipulating Haskell source: abstract syntax, lexer, parser, and pretty-
printer https://github.com/haskell-suite/haskell-src-exts  
haskell-src-exts \  
# > Combinator library for splitting lists.  
split \  
# > Anaphoric and miscellaneous useful control-flow  
ifelse \  
# > Lenses, Folds and Traversals http://github.com/ekmett/lens/  
lens \  
# > Backend for the persistent library using sqlite3.
http://www.yesodweb.com/book/persistent  
persistent-sqlite \  
# > Type-safe, non-relational, multi-backend persistence.
http://www.yesodweb.com/book/persistent  
persistent-template \  
# > Monadic parser combinators https://github.com/hvr/parsec  
parsec \  
;  
  
  
COPY rootfs/runner /runner  
WORKDIR /workspace  

