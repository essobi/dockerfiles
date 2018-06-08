FROM invokr/cgit  
  
# cgit about page is written by markdown, support it  
RUN yum install -y python-markdown python-pygments  
  
# Avoid cgi error: Error reading repo owner..  
# My git repo uid is 1001  
RUN groupadd -g 1001 git && useradd -g git -u 1001 git  
# elsdoer/gitolite's git uid is 103, gid=106  
RUN groupadd -g 106 gitolite && useradd -g 106 -u 103 gitolite  
  
ADD scripts/init.sh /opt/init.sh  
  
# Make default config workable  
ADD config/cgit.conf /etc/cgit/cgitrc  
  

