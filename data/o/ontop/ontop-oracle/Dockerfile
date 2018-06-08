  
FROM sath89/oracle-12c:r1  
  
  
# copying all SQL files to this folder will automatically put them in the
default DB  
COPY sql/*.sql /docker-entrypoint-initdb.d/  
  
  
# docker build -t ontop_oracle .  
  
  
# docker pull sath89/oracle-12c  
  
# based one https://store.docker.com/community/images/sath89/oracle-12c  
  
# Connect with :  
# hostname: localhost  
# port: 1521  
# sid: xe  
# service name: xe.oracle.docker  
# username: system  
# password: oracle  
  
# Run with 8080 and 1521 ports opened:  
# docker run -d -p 8080:8080 -p 1521:1521 sath89/oracle-12c  
  
# To connect using sqlplus:  
# sqlplus system/oracle@//localhost:1521/xe.oracle.docker  
  
# To Run with Custom DBCA_TOTAL_MEMORY (in Mb):  
# docker run -d -p 8080:8080 -p 1521:1521 -v /my/oracle/data:/u01/app/oracle
-e DBCA_TOTAL_MEMORY=1024 sath89/oracle-12c  
  
# to be connected remotely  
# docker run -d -p 49160:22 -p 49161:1521 -e ORACLE_ALLOW_REMOTE=true
wnameless/oracle-xe-11g  
  
# password for SYS & SYSTEM = oracle  
  
# Start with additional init scripts or dumps:  
# docker run -d -p 1521:1521 -v /my/oracle/data:/u01/app/oracle -v
/my/oracle/init/SCRIPTSorSQL:/docker-entrypoint-initdb.d sath89/oracle-12c  

