FROM clojure as clojure  
  
COPY clj-tools/spacedoc /usr/src/app  
  
RUN cd /usr/src/app && lein uberjar  
  
FROM ubuntu as graalvm  
  
ENV GRAALVM_V=1.0.0-rc1  
  
WORKDIR /tmp  
  
COPY \--from=clojure /usr/src/app/target/uberjar/sdn.jar ./  
  
RUN apt-get update && apt-get install -y wget gcc libz-dev  
  
RUN wget --quiet
https://github.com/oracle/graal/releases/download/vm-${GRAALVM_V}/graalvm-
ce-${GRAALVM_V}-linux-amd64.tar.gz \  
&& tar -xvzf graalvm-ce-${GRAALVM_V}-linux-amd64.tar.gz  
  
RUN graalvm-${GRAALVM_V}/bin/native-image --no-server
-H:+ReportUnsupportedElementsAtRuntime -jar /tmp/sdn.jar  
  
FROM jare/emacs  
  
COPY \--from=graalvm /tmp/sdn /usr/local/bin  
  
COPY . /opt/spacedoc  
  
RUN chmod 775 /usr/local/bin/sdn \  
/opt/spacedoc/run \  
/opt/spacedoc/emacs-tools/docfmt/run.el \  
/opt/spacedoc/emacs-tools/export/run.el  
  
RUN ln -s /opt/spacedoc/emacs-tools/export/target/ /tmp/export  
  
ENTRYPOINT ["/opt/spacedoc/run"]  
  
CMD ["--help"]  

