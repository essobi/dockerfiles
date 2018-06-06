FROM docker:17.05  
ENV GLIBC 2.25-r0  
  
ADD https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub /etc/apk/keys/sgerrand.rsa.pub  
ADD https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC/glibc-$GLIBC.apk glibc-$GLIBC.apk  
  
RUN apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk && \  
ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \  
ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib  
  
RUN apk -v --update add \  
python \  
py-pip \  
groff \  
less \  
mailcap \  
gettext \  
&& \  
pip install --upgrade awscli s3cmd python-magic && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  
  
ADD https://downloads.dcos.io/binaries/cli/linux/x86-64/dcos-1.9/dcos
/usr/local/bin/dcos  
ADD https://github.com/Originate/dcos-login/releases/download/v0.24/dcos-
login_linux_amd64 /usr/local/bin/dcos-login  
  
RUN chmod +x /usr/local/bin/dcos && \  
chmod +x /usr/local/bin/dcos-login  
  
CMD ["sh"]  

