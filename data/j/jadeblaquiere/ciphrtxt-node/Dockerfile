# ciphrtxt-test  
FROM jadeblaquiere/ciphrtxt-base-os  
  
# TODO: Put the maintainer name in the image metadata  
MAINTAINER Joseph deBlaquiere <jadeblaquiere@yahoo.com>  
  
# TODO: Rename the builder environment variable to inform users about
application you provide them  
ENV BUILDER_VERSION 0.1  
# TODO: Set the default port for applications built using this image  
EXPOSE 7754  
EXPOSE 7764  
# TODO: Set the default CMD for the image  
# CMD ["usage"]  
ENV GOPATH /home/ciphrtxt  
ENV RPCUSERNAME rpcuser  
ENV RPCPASSWORD rpcpass  
ENV EXTHOSTNAME localhost  
ENV MININGPUBKEY CKxrrgp9r62FMwVZUGd2x3dnnhLzpYzQZk  
ENV NAKPRIV ca92102f1fde262153ceeeaff7f5e4e98077dfb2adfa829e69581d0115acb83c  
  
#install ctcd  
ENV PATH /usr/lib/go-1.6/bin:$PATH  
RUN go get -u github.com/Masterminds/glide  
RUN go get github.com/jadeblaquiere/ctcd  
RUN (cd /home/ciphrtxt/src/github.com/jadeblaquiere/ctcd && go install .
./cmd/ctcctl/... )  
  
# install msgstore  
RUN (cd /home/ciphrtxt && git clone
https://github.com/jadeblaquiere/msgstore.git)  
  
RUN echo "#!/usr/bin/env sh" > /home/ciphrtxt/run.sh  
RUN echo "if [ \$EXTHOSTNAME = \"localhost\" ] && [
\$DOCKERCLOUD_CONTAINER_FQDN != \"\" ] ; then export
EXTHOSTNAME=\$DOCKERCLOUD_CONTAINER_FQDN ; fi" >> /home/ciphrtxt/run.sh  
RUN echo "(cd /home/ciphrtxt/msgstore && python3 ./app.py
--rpcuser=\$RPCUSERNAME --rpcpass=\$RPCPASSWORD --exthost=\$EXTHOSTNAME
--nakpriv=\$NAKPRIV & )" >> /home/ciphrtxt/run.sh  
RUN echo "sleep 5 ; /home/ciphrtxt/bin/ctcd --nodnsseed --addpeer
indigo.ciphrtxt.com --addpeer indigo.bounceme.net --addpeer
violet.ciphrtxt.com --txindex --rpcuser=\$RPCUSERNAME --rpcpass=\$RPCPASSWORD
--miningaddr \$MININGPUBKEY" >> /home/ciphrtxt/run.sh  
  
RUN chmod 755 /home/ciphrtxt/run.sh  
  
CMD /home/ciphrtxt/run.sh  

