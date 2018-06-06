FROM alpine:3.6  
MAINTAINER Molindo GmbH <build@molindo.at>  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV JAVA_OPTS ""  
ENV JAVA_ARGS ""  
RUN set -x \  
&& apk add --no-cache curl bash wget gnupg openjdk8-jre \  
&& echo -e '#!/bin/sh\nexec /usr/bin/java -XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap $JAVA_OPTS "$@" $JAVA_ARGS' >
/usr/local/bin/java.sh \  
&& chmod +x /usr/local/bin/* \  
&& /usr/local/bin/java.sh -version  
  
ENTRYPOINT ["/usr/local/bin/java.sh"]  
CMD ["-version"]  

