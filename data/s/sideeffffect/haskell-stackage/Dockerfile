## Dockerfile for a haskell environment, with lts stackage  
FROM haskell:7.8  
MAINTAINER Ondra Pelech <ondra.pelech@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y freeglut3-dev \  
libblas-dev \  
libbz2-dev \  
libcairo2-dev \  
libglib2.0-dev \  
libgsl0-dev \  
libicu-dev \  
liblapack-dev \  
libmysqlclient-dev \  
libncurses5-dev \  
libpango1.0-dev \  
libpcre3-dev \  
libpq-dev \  
libtinfo-dev \  
libxrandr-dev \  
libxss-dev \  
libzmq3-dev \  
llvm \  
llvm-dev \  
nettle-dev \  
opt \  
pkg-config \  
libcurl4-openssl-dev \  
libfreenect-dev \  
libgd-dev \  
libgtk2.0-dev \  
libgtk-3-dev \  
liblzma-dev \  
libnotify-dev  
  
RUN cabal info  
RUN curl -sf -L "https://www.stackage.org/lts/2/cabal.config?global=true" >>
/root/.cabal/config  
RUN cabal update  
  
RUN which ghc && \  
ghc --version && \  
which cabal && \  
cabal --version && \  
ghc-pkg list  
  
RUN cabal install cabal-install  
RUN cabal install alex happy  
RUN cabal install cpphs gtk2hs-buildtools  
RUN cabal install array \  
async \  
attoparsec \  
base \  
bytestring \  
case-insensitive \  
containers \  
deepseq \  
directory \  
extensible-exceptions \  
fgl \  
filepath \  
GLURaw \  
GLUT \  
hashable \  
haskell2010 \  
haskell98 \  
hpc \  
hscolour \  
html \  
HTTP \  
HUnit \  
mtl \  
network \  
old-locale \  
old-time \  
OpenGL \  
OpenGLRaw \  
parallel \  
parsec \  
pretty \  
primitive \  
process \  
QuickCheck \  
random \  
regex-base \  
regex-compat \  
regex-posix \  
split \  
stm \  
syb \  
template-haskell \  
text \  
time \  
transformers \  
unix \  
unordered-containers \  
vector \  
xhtml \  
zlib  
  
RUN which ghc && \  
ghc --version && \  
which cabal && \  
cabal --version && \  
ghc-pkg list  
  
## run ghci by default unless a command is specified  
CMD ["ghci"]  
  

