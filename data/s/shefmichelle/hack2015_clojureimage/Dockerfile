FROM clojure  
COPY . /usr/src/app  
WORKDIR /usr/src/app/runner  
RUN [ "lein", "run" ]  
WORKDIR /usr/src/app  
ENTRYPOINT [ "bash", "run.sh" ]

