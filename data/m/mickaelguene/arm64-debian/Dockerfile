FROM scratch  
MAINTAINER Mickael Guene <mickael.guene@st.com>  
  
ADD arm64-debian-jessie.tgz /  
ADD configure.sh /configure.sh  
RUN ["/usr/bin/umeq-arm64", "-execve", "-0", "bash", "/bin/bash", "-c",
"/configure.sh"]  
  
CMD ["/usr/bin/umeq-arm64", "-execve", "-0", "bash", "/bin/bash"]  

