FROM java:openjdk-8  
MAINTAINER Raymond Kroon <raymond@k3n.nl>  
  
RUN apt-get update && apt-get install -y --no-install-recommends bash git &&
rm -rf /var/lib/apt/lists/*  
  
RUN useradd --create-home --home-dir /home/user user && chown -R user:user
/home/user  
  
USER user  
WORKDIR /home/user  
  
ENV BOOT_VERSION 2.5.2  
RUN mkdir bin && wget -O bin/boot https://github.com/boot-clj/boot-
bin/releases/download/2.5.2/boot.sh && chmod +x bin/boot  
  
#preload boot  
RUN bin/boot  
  
ENV BOOT_EMIT_TARGET no  
  
#mount points for app and maven cache  
WORKDIR /home/user/app  
VOLUME /home/user/app /home/user/.m2  
  
ENTRYPOINT ["/home/user/bin/boot"]  

