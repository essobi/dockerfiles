FROM ubuntu:14.04  
MAINTAINER Enis Afgan <enis.afgan@jhu.edu>  
  
# Setup the system  
RUN apt-get update -qq --fix-missing; \  
apt-get install -qq -y wget python python-pip python-dev zlib1g-dev;  
  
RUN pip install numpy  
RUN pip install bx-python  
RUN pip install http://depot.galaxyproject.org/package/source/gops-1.0.tgz  
  
RUN mkdir /tools  
  
# Install Join tool  
RUN wget -O /tools/gops_join.py
https://raw.githubusercontent.com/galaxyproject/tools-
devteam/d155d6caf747a7c59ebd6d5752c942e63a75939f/tool_collections/gops/join/gops_join.py  
RUN ln -s /tools/gops_join.py /usr/bin  
RUN chmod a+x /tools/gops_join.py  
  
# Install Sort tool  
RUN wget -O /tools/sorter.py https://bitbucket.org/galaxy/galaxy-
central/raw/37fb229769f4a1cc02d7df26790c5c6f13e913d6/tools/filters/sorter.py  
# Add the shebang line to the script to make it standalone  
RUN sed -i '1s/^/#!\/usr\/bin\/env python\n/' /tools/sorter.py  
RUN ln -s /tools/sorter.py /usr/bin  
RUN chmod a+x /tools/sorter.py  
  
# Install Grouping tool  
RUN wget -O /tools/grouping.py https://bitbucket.org/galaxy/galaxy-
central/raw/37fb229769f4a1cc02d7df26790c5c6f13e913d6/tools/stats/grouping.py  
RUN ln -s /tools/grouping.py /usr/bin  
RUN chmod a+x /tools/grouping.py  
  
# Install Compare tool  
RUN wget -O /tools/joinWrapper.py https://bitbucket.org/galaxy/galaxy-
central/raw/37fb229769f4a1cc02d7df26790c5c6f13e913d6/tools/filters/joinWrapper.py  
RUN ln -s /tools/joinWrapper.py /usr/bin  
RUN chmod a+x /tools/joinWrapper.py  
  
# Install 'Select first' tool  
RUN wget -O /tools/headWrapper.pl
https://raw.githubusercontent.com/galaxyproject/tools-
devteam/d155d6caf747a7c59ebd6d5752c942e63a75939f/tools/show_beginning/headWrapper.pl  
RUN ln -s /tools/headWrapper.pl /usr/bin  
RUN chmod a+x /tools/headWrapper.pl  

