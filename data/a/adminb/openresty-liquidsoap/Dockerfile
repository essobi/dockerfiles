# Builds the Liquidsoup and Openresty  
# escape=\  
FROM ocaml/opam:debian-stable_ocaml-4.05.0  
  
# Set up dependencies  
  
USER root  
  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN curl -s https://openresty.org/package/pubkey.gpg | apt-key add \- \  
&& echo "deb http://deb.debian.org/debian stable main contrib non-free" >
/etc/apt/sources.list \  
&& apt-get -y install software-properties-common \  
&& sudo add-apt-repository -y "deb http://openresty.org/package/debian
$(lsb_release -sc) openresty" \  
&& apt-get update \  
&& apt-get install -y apt-utils \  
# use this line if you want to get resty cmd line and other utils  
# && apt-get install -y openresty \  
&& apt-get install -y \--no-install-recommends openresty \  
&& apt-get install -y \  
libmad0-dev libmp3lame-dev libogg-dev libpcre3-dev \  
libsamplerate0-dev libssl-dev libtag1-dev \  
libopus-dev libvorbis-dev libfdk-aac-dev libflac-dev \  
netcat jq  
  
# give permissions for user opam  
RUN mkdir /var/log/liquidsoap /var/log/nginx \  
&& chown -R opam:opam /var/log/liquidsoap /var/log/nginx \  
&& chmod 766 /var/log/liquidsoap /var/log/nginx  
  
USER opam  
  
# Initialize OPAM and install Liquidsoap and asssociated packages  
  
RUN opam update \  
&& eval `opam config env` \  
&& opam install -y ssl opus cry flac inotify lame mad ogg fdkaac samplerate
taglib vorbis xmlplaylist liquidsoap  
  
# Expose ports for harbor connections and telnet server, respectively  
EXPOSE 8111  
EXPOSE 8080  
EXPOSE 8011  
  
USER root  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
  
ENTRYPOINT [ "/usr/local/openresty/nginx/sbin/nginx", "-g", "daemon off;",
"-c", "/etc/nginx.conf" ]

