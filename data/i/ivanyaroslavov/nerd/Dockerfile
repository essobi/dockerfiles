FROM clojure  
MAINTAINER Ivan Yaroslavov Stefanov <ivan.yaroslavov@vne.io>  
  
COPY . /opt/vne-src  
COPY /products/diameter/product_settings.clj /opt/vne-src/resources/  
  
ARG META_PASS  
  
RUN chmod +x /opt/vne-src/update-metadata.sh  
RUN rm -rf /opt/vne-src/resources/public/js/* \  
&& cd /opt/vne-src \  
&& ./update-metadata.sh $META_PASS \  
&& lein clean \  
&& lein garden once \  
&& lein with-profile uberjar cljsbuild once \  
&& lein uberjar \  
&& cd / \  
&& mkdir -p /opt/vne \  
&& mkdir -p /opt/vne/logs \  
&& cp /opt/vne-src/target/vne-io.jar /opt/vne \  
&& cp /opt/vne-src/.lein-env /opt/vne \  
&& rm -rf /opt/vne-src  
  
WORKDIR /opt/vne  
EXPOSE 9090  
CMD java -jar vne-io.jar  

