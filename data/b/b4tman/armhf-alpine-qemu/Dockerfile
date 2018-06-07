FROM golang:alpine as build  
  
WORKDIR /tmp/build  
  
COPY resin-xbuild.go /tmp/build  
  
RUN go build -ldflags "-w -s" resin-xbuild.go  
  
RUN apk add --no-cache curl  
  
ENV QEMU_RELEASE_TAG v2.9.0+resin1  
ENV QEMU_RELEASE_FILE qemu-2.9.0.resin1-arm.tar.gz  
ENV QEMU_RELEASE_SHA256
b39d6a878c013abb24f4cccc7c3a79829546ae365069d5712142a4ad21bcb91b  
  
RUN QEMU_URL="https://github.com/resin-
io/qemu/releases/download/${QEMU_RELEASE_TAG}/${QEMU_RELEASE_FILE}" ; \  
curl -fsSL ${QEMU_URL} -o ${QEMU_RELEASE_FILE}  
  
RUN echo "${QEMU_RELEASE_SHA256} ${QEMU_RELEASE_FILE}" >
${QEMU_RELEASE_FILE}.sha256sum \  
sha256sum -c ${QEMU_RELEASE_FILE}.sha256sum  
  
RUN tar --strip 1 -xzf ${QEMU_RELEASE_FILE}  
  
FROM container4armhf/armhf-alpine:3.5  
ENV QEMU_EXECVE 1  
COPY \--from=build /tmp/build/qemu-arm-static /usr/bin  
COPY \--from=build /tmp/build/resin-xbuild /usr/bin  
  
RUN [ "/usr/bin/qemu-arm-static", "/bin/sh", "-exc", "ln -s resin-xbuild
/usr/bin/cross-build-start; ln -s resin-xbuild /usr/bin/cross-build-end; ln
/bin/sh /bin/sh.real" ]  

