FROM clojure  
MAINTAINER Ivan Yaroslavov Stefanov <ivan.yaroslavov@vne.io>  
  
COPY . /opt/vne-src  
COPY ./resources/samples /samples  
COPY /products/voipgw/product_settings.clj /opt/vne-src/resources/  
  
ARG META_PASS  
  
RUN chmod +x /opt/vne-src/update-metadata.sh  
RUN rm -rf /opt/vne-src/resources/public/js/* \  
&& cd /opt/vne-src \  
&& ./update-metadata.sh $META_PASS \  
&& lein clean \  
&& lein deploy voicerss.project voicerss 0.0.1 voicerss_tts.jar \  
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
EXPOSE 9090-9092  
CMD java -jar \  
-Dportal_cert_pass=${PORTAL_CERT_PASS} \  
-Dportal_cert_path=${PORTAL_CERT_PATH} \  
-Dvneio_portal_name=${VNEIO_PORTAL_NAME} \  
vne-io.jar  

