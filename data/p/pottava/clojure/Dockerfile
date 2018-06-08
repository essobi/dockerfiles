# Clojure v1.8 (REPL)  
# docker run --rm -it pottava/clojure:repl  
FROM pottava/java:8  
ENV CLOJURE_VERSION=1.8.0  
RUN set -e \  
&& apk --no-cache add --virtual build-dependencies curl unzip \  
&& mkdir -p /usr/lib/clojure \  
&& cd /usr/lib/clojure \  
&& curl -O --location --silent --show-error
http://repo1.maven.org/maven2/org/clojure/clojure/${CLOJURE_VERSION}/clojure-${CLOJURE_VERSION}.zip
\  
&& unzip -q clojure-${CLOJURE_VERSION}.zip \  
&& rm -rf clojure-${CLOJURE_VERSION}.zip \  
clojure-${CLOJURE_VERSION}/changes.md \  
clojure-${CLOJURE_VERSION}/doc \  
clojure-${CLOJURE_VERSION}/epl-v10.html \  
clojure-${CLOJURE_VERSION}/readme.txt \  
clojure-${CLOJURE_VERSION}/src \  
clojure-${CLOJURE_VERSION}/test \  
&& apk del --purge build-dependencies  
  
ENTRYPOINT ["java"]  
CMD ["-cp",
"/usr/lib/clojure/clojure-${CLOJURE_VERSION}/clojure-${CLOJURE_VERSION}.jar",
"clojure.main"]  

