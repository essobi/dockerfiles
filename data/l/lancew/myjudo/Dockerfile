FROM alpine:3.7  
  
RUN apk add --no-cache curl gcc git libressl-dev linux-headers make musl-dev
perl sqlite-libs  
  
# Install Perl 6  
RUN curl -L https://github.com/rakudo/rakudo/archive/2018.05.tar.gz \  
| tar xzf - \  
&& cd rakudo-2018.05 \  
&& perl Configure.pl --backend=moar --gen-moar --prefix=/usr \  
&& make -j`nproc` install  
  
# Install zef  
RUN git clone https://github.com/ugexe/zef.git \  
&& cd zef \  
&& perl6 -Ilib bin/zef install --/test .  
  
WORKDIR /app  
  
COPY META6.json .  
  
RUN /usr/share/perl6/site/bin/zef install --deps-only --/test .  
  
# Avoid having "binaries" in the final image  
RUN rm -r /usr/share/perl6/site/bin  
  
FROM scratch  
  
COPY --from=0 /bin/sh /bin/  
COPY --from=0 /lib/ld-musl-x86_64.so.1 \  
/lib/libz.* /lib/  
COPY --from=0 /usr/bin/moar \  
/usr/bin/perl6 /usr/bin/  
COPY --from=0 /usr/lib/libmoar.so \  
/usr/lib/libcrypto.* \  
/usr/lib/libsqlite3.* \  
/usr/lib/libssl.* /usr/lib/  
COPY --from=0 /usr/share/nqp /usr/share/nqp  
COPY --from=0 /usr/share/perl6 /usr/share/perl6  
  
WORKDIR /app  
  
COPY . /app  
  
CMD ["perl6", "-Ilib", "service.p6"]  

