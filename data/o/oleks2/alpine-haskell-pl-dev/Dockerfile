# Copyright 2017 oleks <oleks@oleks.info>  
#  
# Licensed under the Apache License, Version 2.0 (the "License"); you may not  
# use this file except in compliance with the License. A copy of the License  
# text is included alongside this file as LICENSE.md.  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT  
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  
# License for the specific language governing permissions and limitations
under  
# the License.  
FROM mitchty/alpine-ghc:8.0.2  
  
ARG username=ghc  
  
MAINTAINER oleks <oleks@oleks.info>  
  
RUN adduser -D -u 1000 ${username}  
WORKDIR /home/${username}/  
  
RUN apk --no-cache add \  
\--virtual .build-dependencies \  
alpine-sdk  
  
USER ${username}  
RUN cabal update && \  
cabal install \  
parsec \  
happy \  
hlint  
  
USER root  
RUN apk del .build-dependencies  
  
USER ${username}  
  
CMD ["ghci"]  

