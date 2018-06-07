FROM centos:7  
ENV svt_go_version 0.0.1  
ENV build_number travis_57  
RUN mkdir /myapp  
WORKDIR /myapp  
RUN curl -o svt-${svt_go_version}-Linux-x86_64.tar.gz
"https://raw.githubusercontent.com/cduser/svt-
release/${build_number}/svt-${svt_go_version}-Linux-x86_64.tar.gz" && tar -xzf
"svt-${svt_go_version}-Linux-x86_64.tar.gz"  
CMD ["./svt/svt", "http"]  

