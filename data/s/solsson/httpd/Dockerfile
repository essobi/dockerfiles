  
FROM httpd:2.4.23  
ENV GIT_VERSION 2.9.3  
ENV GIT_VERSION_TGZ_URL
https://www.kernel.org/pub/software/scm/git/git-$GIT_VERSION.tar.gz  
ENV GIT_VERSION_TGZ_SHA1 ae90c4e5008ae10c8a67a51ff3dbea8364d97168  
  
RUN depsRuntime=' \  
libcurl3 \  
libexpat1 \  
gettext \  
libssl1.0.0 \  
' \  
&& depsBuild=' \  
curl ca-certificates \  
gcc \  
make \  
autoconf \  
libcurl4-gnutls-dev \  
libexpat1-dev \  
gettext \  
libz-dev \  
libssl-dev \  
' \  
set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $depsRuntime \  
&& apt-get install -y --no-install-recommends $depsBuild \  
&& rm -r /var/lib/apt/lists/* \  
&& curl -SL "$GIT_VERSION_TGZ_URL" -o git-$GIT_VERSION.tar.gz \  
&& echo "$GIT_VERSION_TGZ_SHA1 git-$GIT_VERSION.tar.gz" | sha1sum -c - \  
&& mkdir -p src/git \  
&& tar -xvf git-$GIT_VERSION.tar.gz -C src/git --strip-components=1 \  
&& rm git-$GIT_VERSION.tar.gz* \  
&& cd src/git \  
&& make configure \  
&& ./configure --prefix=/usr \  
&& make all \  
&& make install \  
&& cd ../../ \  
&& rm -r src/git \  
&& apt-get purge -y --auto-remove $depsBuild  
  
EXPOSE 80  
RUN sed -i 's|#LoadModule cgid_module|LoadModule cgid_module|' conf/httpd.conf
\  
&& sed -i 's|#LoadModule rewrite_module|LoadModule rewrite_module|'
conf/httpd.conf \  
&& echo "Include conf/git/*.conf" >> conf/httpd.conf  
  
ADD conf/git.conf /usr/local/apache2/conf/git/  
ADD conf/git-readonly.conf /usr/local/apache2/conf/git/  

