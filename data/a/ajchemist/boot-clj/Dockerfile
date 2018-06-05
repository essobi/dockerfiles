FROM ajchemist/openjdk:8-jre-alpine  
MAINTAINER aJchemist <ajchemist@turingmind.com>  
  
ARG BOOTCLJ_URL=https://github.com/boot-clj/boot-
bin/releases/download/latest/boot.sh  
  
RUN apk add --update --no-cache bash curl  
  
RUN curl -Lo /usr/bin/boot ${BOOTCLJ_URL} \  
&& chmod +x /usr/bin/boot;  
  
ENV BOOT_AS_ROOT yes  
ENV BOOT_EMIT_TARGET no  
ENV BOOT_CLOJURE_NAME org.clojure/clojure  
ENV BOOT_HOME /.boot  
ENV BOOT_LOCAL_REPO /m2/repository  
ENV BOOT_JVM_OPTIONS=-Xmx2g  
  
# download & install deps, cache REPL and web deps  
# RUN /usr/bin/boot web -s doesnt/exist repl -e '(System/exit 0)' && rm -rf
target  
ENTRYPOINT ["/usr/bin/boot"]  

