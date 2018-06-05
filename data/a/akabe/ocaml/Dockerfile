FROM alpine:3.5  
ENV OPAM_VERSION 1.2.2  
ENV OCAML_VERSION 4.00.1  
ENV HOME /home/opam  
  
RUN apk update && \  
apk upgrade && \  
apk add --upgrade --no-cache alpine-sdk libx11-dev && \  
mkdir /lib64 && \  
ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \  
adduser -h $HOME -s /bin/sh -D opam && \  
\  
echo 'opam ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers && \  
curl -s -L -o /usr/bin/opam
"https://github.com/ocaml/opam/releases/download/$OPAM_VERSION/opam-$OPAM_VERSION-$(uname
-m)-$(uname -s)" && \  
chmod 755 /usr/bin/opam && \  
su opam -c "opam init -a -y --comp $OCAML_VERSION" && \  
rm $HOME/.profile $HOME/.opam/opam-init/init.* && \  
find $HOME/.opam -regex '.*\\\\.\\\\(cmt\\\|cmti\\\|annot\\\|byte\\\\)'
-delete && \  
rm -rf $HOME/.opam/archives \  
$HOME/.opam/repo/default/archives \  
$HOME/.opam/$OCAML_VERSION/build  
  
USER opam  
WORKDIR $HOME  
  
ENTRYPOINT [ "opam", "config", "exec", "--" ]  
CMD [ "sh" ]  

