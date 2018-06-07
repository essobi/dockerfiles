FROM circleci/python:2.7.14-jessie  
  
USER root  
  
# install terraform  
RUN wget
https://releases.hashicorp.com/terraform/0.9.9/terraform_0.9.9_linux_amd64.zip
&& \  
unzip terraform_0.9.9_linux_amd64.zip && \  
rm -f terraform_0.9.9_linux_amd64.zip && \  
mv terraform /usr/local/bin  
  
# install aws cli  
RUN wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip && \  
unzip awscli-bundle.zip && \  
rm -f awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm -r awscli-bundle  
  
# install bats for testing  
RUN git clone https://github.com/sstephenson/bats.git && \  
cd bats && \  
./install.sh /usr/local && \  
cd .. && \  
rm -rf bats  
  
# install dependencies for tap-to-junit  
RUN perl -MCPAN -e "install TAP::Parser" && \  
perl -MCPAN -e "install XML::Generator"  
  
# install tap-to-junit  
RUN git clone https://github.com/jmason/tap-to-junit-xml.git  
  
USER circleci

