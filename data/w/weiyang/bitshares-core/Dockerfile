  
FROM ubuntu:16.04  
ENV REPO bitshares/bitshares-core  
ENV REPO_DIR bitshares-core  
ENV BUILD_DEP curl jq g++ libtool autoconf cmake git libboost-all-dev libssl-
dev  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y ${BUILD_DEP}\  
&& git clone https://github.com/${REPO} \  
&& cd ${REPO_DIR} \  
&& git checkout $(curl -sSL
https://api.github.com/repos/${REPO}/releases/latest | jq --raw-output
'.tag_name') \  
&& git submodule update --init --recursive \  
&& cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo . \  
&& make \  
&& mv ./programs/witness_node/witness_node /usr/bin/ \  
&& mv ./programs/cli_wallet/cli_wallet /usr/bin/ \  
&& rm -rf /${REPO_DIR} \  
&& apt-get remove -y ${BUILD_DEP} \  
&& apt-get clean \  
&& apt-get autoremove -y  
  
CMD ["witness_node"]  

