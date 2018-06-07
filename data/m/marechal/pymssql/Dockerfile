FROM fedora  
  
RUN yum update -y  
RUN yum install -y vim python python-pip freetds gcc-c++  
  
RUN pip install pymssql jinja2 pandas pyyaml XlsxWriter  
  
ADD ./freetds.conf /etc/freetds.conf  
RUN chmod 444 /etc/freetds.conf  
  
CMD "/bin/bash"  

