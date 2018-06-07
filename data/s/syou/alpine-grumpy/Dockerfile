FROM syou/alpine-grumpy-base  
  
MAINTAINER S-YOU<S-YOU@users.noreply.github.com>  
  
ENV PYTHONPATH=/src/grumpy-master/build/site-packages:/src/grumpy-
master/build/lib/python2.7/site-packages/ \  
GOPATH=/src/grumpy-master/build:/src/grumpy-
master/build/pkg/linux_amd64:/usr/lib/go/pkg/linux_amd64:/usr/lib/go/pkg/linux_amd64_shared
\  
PATH=$PATH:/src/grumpy-master/build/bin/ \  
CGOENABLED=0 \  
PYTHONDONTWRITEBYTECODE=1  
  
RUN apk add --no-cache openssl make \  
&& mkdir -p /src/app && cd /src \  
&& wget -qO- https://codeload.github.com/google/grumpy/tar.gz/master | tar zx
\  
&& cd grumpy-master \  
&& sed -ri 's: -pack : -I usr/lib/go/pkg/linux_amd64 -I
/usr/lib/go/pkg/linux_amd64_shared -pack :' Makefile \  
&& make \  
&& cp tools/grumprun build/bin/ \  
&& ls | grep -v build | xargs rm -rf \  
&& apk del openssl make \  
&& chown guest:nogroup /src/app  
  
USER guest  
  
WORKDIR /src/app  
  

