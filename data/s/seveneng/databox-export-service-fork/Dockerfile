FROM alpine:3.5  
LABEL distro_style="apk" distro="alpine" distro_long="alpine" arch="x86_64"
ocaml_version="4.04.0" opam_version="1.2" operatingsystem="linux"  
  
RUN apk update && apk upgrade \  
&& apk add alpine-sdk bash ncurses-dev \  
&& adduser -S databox \  
&& echo 'databox ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/databox \  
&& chmod 440 /etc/sudoers.d/databox \  
&& chown root:root /etc/sudoers.d/databox \  
&& sed -i.bak 's/^Defaults.*requiretty//g' /etc/sudoers  
  
USER databox  
WORKDIR /home/databox  
  
ADD . databox-export-service  
  
RUN sudo apk add opam \  
&& cd databox-export-service \  
&& sudo chmod +x install.sh && sync \  
&& ./install.sh \  
&& sudo apk del opam  
  
EXPOSE 8080  
LABEL databox.type="export-service"  
  
ENTRYPOINT ["./export-service"]

