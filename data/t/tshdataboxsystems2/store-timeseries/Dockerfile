FROM ocaml/opam:alpine_ocaml-4.04.2  
# add the code  
ADD src src  
RUN sudo chown -R opam:nogroup src  
# add the build script  
ADD build.sh .  
  
# setup ocaml  
RUN sudo apk update && sudo apk add alpine-sdk bash ncurses-dev m4 perl gmp-
dev zlib-dev libsodium-dev opam \  
&& opam pin add -n opium https://github.com/me-box/opium.git#fix-ssl-option \  
&& opam pin add -n sodium https://github.com/me-box/ocaml-
sodium.git#with_auth_hmac256 \  
&& opam install -y reason.1.13.7 lwt tls sodium macaroons opium cohttp ezirmin
bos uuidm \  
&& sudo chmod +x build.sh && sync \  
&& ./build.sh \  
&& rm -rf /home/opam/src \  
&& rm -rf /home/opam/.opam \  
&& rm -rf /home/opam/opam-repository  
  
FROM alpine:latest  
  
USER root  
WORKDIR /home/databox  
  
COPY \--from=0 /home/opam/ .  
  
# runtime dependencies  
RUN apk update && apk upgrade \  
&& apk add libsodium gmp zlib  
  
USER root  
VOLUME /database  
  
EXPOSE 8080  
LABEL databox.type="store"  
  
ENTRYPOINT ["./main.exe"]  

