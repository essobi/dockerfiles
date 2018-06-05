FROM circleci/ruby:2.4.1-node-browsers  
  
RUN sudo apt-get update -qq && sudo apt-get install -y build-essential libpq-
dev libaio1 unzip  
  
RUN sudo mkdir /opt/oracle  
ADD *.zip /opt/oracle/  
RUN cd /opt/oracle && sudo unzip -q \\*.zip  
RUN cd /opt/oracle/instantclient_12_2 && sudo ln -s libclntsh.so.12.1
libclntsh.so  
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_12_2  
  
RUN gem install ruby-oci8  

