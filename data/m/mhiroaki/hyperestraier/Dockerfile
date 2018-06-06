FROM debian:stable  
  
RUN groupadd --gid 1000 app && useradd --uid 1000 --gid app app  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends hyperestraier \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 1978  
ENV HEDIR /he  
WORKDIR $HEDIR  
VOLUME $HEDIR  
  
USER app  

