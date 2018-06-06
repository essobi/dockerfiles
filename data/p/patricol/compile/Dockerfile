FROM alpine:latest as alpine  
  
ENV OPAMYES=true  
  
RUN apk update && \  
apk add opam make bash build-base abuild && \  
opam init && \  
opam install depext && \  
opam depext google-drive-ocamlfuse && \  
opam install google-drive-ocamlfuse && \  
mv /root/.opam/system/bin/google-drive-ocamlfuse /  
  
FROM scratch  
COPY --from=alpine /google-drive-ocamlfuse /google-drive-ocamlfuse

