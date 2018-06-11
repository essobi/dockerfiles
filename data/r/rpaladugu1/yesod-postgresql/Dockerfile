# Haskell Yesod Framework based on quick start guide instructions using
stackage exclusive remote repo  
#  
# VERSION 0.0.1  
#Using Haskell minimal toolchain.  
FROM darinmorrison/haskell  
MAINTAINER Ravi K Paladugu <rpaladugu1@gmail.com>  
RUN cabal update  
# Point the cabal remote repo to stackage exclusive link in the cabal config
file  
RUN sed -i "s%^remote-repo: .*%remote-repo:
stackage:http://www.stackage.org/stackage/46bb2d7487546939e22612e7d757f1df5a5163e9%"
/root/.cabal/config  
#Install necessary packages to install yesod and to make postgres work.  
RUN apt-get update && apt-get install -y libpq-dev  
RUN apt-get install -y libghc-zlib-dev libghc-zlib-bindings-dev  
# Now update the cabal package list and install yesod framework  
RUN cabal update && cabal install yesod-bin  
  
#create yesodprojects folder for yesod projects  
RUN mkdir /var/yesodprojects  
RUN cd /var/yesodprojects  
  
# update environment variables  
ENV PATH /root/.cabal/bin:/var/yesodprojects/.cabal-sandbox:$PATH  
#expose port from guest to host  
EXPOSE 3000:3000  
WORKDIR /var/yesodprojects  
RUN printf %s\\\n 'proj1' 'p'| yesod init  
RUN cd proj1 && cabal sandbox init \  
\--sandbox=/var/yesodprojects/.cabal-sandbox \  
&& cabal install --enable-tests --reorder-goals --max-backjumps=-1 -j  
CMD ["bash"]  

