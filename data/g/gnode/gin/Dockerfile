FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
gcc g++ libc6-dev make golang \  
git git-annex openssh-server \  
python-pip python-setuptools \  
bzip2 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install supervisor pyyaml  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 755 "$GOPATH"  
  
RUN go get "github.com/G-Node/gin-repo/..."  
RUN go get "github.com/G-Node/gin-auth/"  
  
#Setting nodes  
RUN curl -sL https://deb.nodesource.com/setup_7.x|bash -  
RUN apt-get install -y nodejs  
RUN mkdir /ui  
WORKDIR /ui  
RUN git clone https://github.com/G-Node/gin-ui.git /ui  
RUN npm install  
RUN npm install vue-template-compiler@2.2.6  
  
# Setting up ssh to tlak to gin  
RUN ln -sf $GOPATH/bin/gin-shell /usr/bin/gin-shell  
COPY ./sshd_config /etc/ssh/  
RUN chmod -R 600 /etc/ssh/ssh_host_rsa_key  
RUN mkdir /var/run/sshd && chmod 755 /var/run/sshd  
  
# git user setup  
RUN addgroup --system git  
RUN adduser --system --home /data --shell /bin/sh --ingroup git --disabled-
password git  
RUN passwd -d git  
  
COPY ./supervisord.conf /etc/supervisord.conf  
EXPOSE 22 8080 8081 8082  
RUN echo ginauth@http://localhost:8081>/data/user.store  
RUN chown -R git:git /data  
  
WORKDIR /data  
ADD ./ /conf  
RUN ln -sf /conf/config.json /ui/src/js/config.json  
VOLUME /data  
VOLUME /conf  
  
ENTRYPOINT supervisord  

