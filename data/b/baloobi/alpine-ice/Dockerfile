# Stage 1 Build Custom Packages  
#  
FROM alpine:3.7  
# Prep work  
RUN apk add -U alpine-sdk pax-utils bash git build-base coreutils tcl-dev
clang \  
gawk readline-dev python3 bison flex libffi-dev mercurial graphviz \  
pkgconfig libftdi1-dev  
COPY abuild.conf /etc/abuild.conf  
COPY APKBUILD.icestorm /APKBUILD.icestorm  
COPY APKBUILD.arachne-pnr /APKBUILD.arachne-pnr  
COPY APKBUILD.yosys /APKBUILD.yosys  
RUN adduser -D builder && addgroup builder abuild && \  
mkdir /packages && chown builder /packages && \  
mkdir /build && chown builder /build && \  
mkdir -p /var/cache/distfiles && chmod a+w /var/cache/distfiles  
  
# Ready the Build tree  
USER builder  
RUN mkdir ~/packages && \  
cd /build && \  
git clone git://git.alpinelinux.org/aports && \  
abuild-keygen -a -n  
USER root  
RUN cp /home/builder/.abuild/*.pub /etc/apk/keys  
RUN cp /home/builder/.abuild/*.pub /packages  
RUN cp /home/builder/.abuild/*.rsa /packages  
  
# Build IceStorm Tools  
USER builder  
RUN cd /build/aports/testing && \  
newapkbuild icestorm && \  
cd icestorm && \  
cp /APKBUILD.icestorm APKBUILD && \  
abuild checksum && \  
abuild -i -k  
RUN mv ~/packages/testing/x86_64/icestorm-1-r0.apk /packages  
  
# Install IceStorm Tools  
USER root  
RUN apk add /packages/icestorm-1-r0.apk  
  
# Build Arachne-PNR  
USER builder  
RUN cd /build/aports/testing && \  
newapkbuild arachne-pnr && \  
cd arachne-pnr && \  
cp /APKBUILD.arachne-pnr APKBUILD && \  
abuild checksum && \  
abuild -i -k  
RUN mv ~/packages/testing/x86_64/arachne-pnr-1-r0.apk /packages  
  
# Build Yosys  
USER builder  
RUN cd /build/aports/testing && \  
newapkbuild yosys && \  
cd yosys && \  
cp /APKBUILD.yosys APKBUILD && \  
abuild checksum && \  
abuild -i -k  
RUN mv ~/packages/testing/x86_64/yosys-1-r0.apk /packages  
  
# Build ttyd  
USER builder  
RUN cd /build/aports/community/ttyd && \  
abuild checksum && \  
abuild -i -k -r  
RUN mv ~/packages/community/x86_64/ttyd-1.4.0-r4.apk /packages  
  
# Build lrzsz  
USER builder  
RUN cd /build/aports/testing/lrzsz && \  
abuild checksum && \  
abuild -i -k  
RUN mv ~/packages/testing/x86_64/lrzsz-0.12.20-r0.apk /packages  
  
# Build iverilog  
USER builder  
RUN cd /build/aports/testing/iverilog && \  
abuild checksum && \  
abuild -i -k -r  
RUN mv ~/packages/testing/x86_64/iverilog-10.2-r0.apk /packages  
  
# Stage 2 Assemble Final Image  
#  
FROM alpine:3.7  
RUN apk --no-cache add git bash  
  
# Add ICETOOLS  
WORKDIR /  
RUN mkdir /packages  
COPY \--from=0 /packages/*.pub /etc/apk/keys/  
COPY \--from=0 /packages/*.apk /packages/  
RUN apk --no-cache add make \  
&& apk add --no-cache /packages/icestorm-1-r0.apk \  
&& apk add --no-cache /packages/arachne-pnr-1-r0.apk \  
&& apk add --no-cache /packages/yosys-1-r0.apk \  
&& apk add --no-cache /packages/ttyd-1.4.0-r4.apk \  
&& apk add --no-cache /packages/lrzsz-0.12.20-r0.apk \  
&& apk add --no-cache /packages/iverilog-10.2-r0.apk \  
&& rm -rf /packages  
  
RUN adduser -D -h /wksp -s /bin/bash builder \  
&& echo 'builder:builder' | chpasswd  
  
COPY ./launcher /bin/  
  
EXPOSE 7681  
ENTRYPOINT ["ttyd"]  
CMD ["launcher"]  

