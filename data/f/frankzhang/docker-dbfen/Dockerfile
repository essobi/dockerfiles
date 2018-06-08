FROM ubuntu:14.04  
MAINTAINER FrankZhang "zjufrankzhang@gmail.com"  
RUN apt-get update && apt-get install -y --force-yes wget curl unzip mysql-
client  
RUN wget http://www.dbfen.com/index.php/help/downclient/dbfen_install.sh  
RUN /bin/bash ./dbfen_install.sh  
  
EXPOSE 40000  
RUN printf "#!/bin/bash\n/usr/local/services/dbfen/startdbfen\n" > run.sh  
RUN printf "/bin/bash" >> run.sh  
RUN chmod +x run.sh  
  
ENTRYPOINT ["./run.sh"]

