FROM cybe/ps-base:alpine37  
  
RUN apk --no-cache add \--virtual .build-deps git go musl-dev binutils \  
# Install sshpiper  
&& export GOPATH=/go \  
&& mkdir -p ${GOPATH}/src ${GOPATH}/bin \  
&& go get -u github.com/tg123/sshpiper/sshpiperd \  
&& strip -s ${GOPATH}/bin/sshpiperd \  
&& mv ${GOPATH}/bin/sshpiperd /usr/local/bin \  
# Cleanup  
&& apk del --purge .build-deps \  
&& rm -rf ${GOPATH}  
  
CMD ["sshpiperd", "--server-key=/ssh-hostkeys/ssh_host_rsa_key", "--port=22",
"--workingdir=/sshpiper"]  

