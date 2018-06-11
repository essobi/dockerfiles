FROM debian:stable  
  
ENV ANSIBLE_VERSION 2.5  
# Install pip and all ansible C prerequisites as debian packages (so no
compiling is needed)  
RUN apt-get update && apt-get install --no-install-recommends -y python-pip
python-cryptography python-bcrypt python-nacl && apt-get clean && rm -Rf
/var/lib/apt/lists  
  
# Install newest minor version of the specified major version  
RUN next_version="`echo ${ANSIBLE_VERSION}|perl -ne 'chomp; print join(".",
splice(@{[split/\\./,$_]}, 0, -1), map {++$_} pop @{[split/\\./,$_]}),
"\n";'`"; \  
pip --no-cache-dir install openshift
"ansible>=${ANSIBLE_VERSION},<${next_version}"  

