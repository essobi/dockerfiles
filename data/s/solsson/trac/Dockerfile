FROM solsson/trac:1.1-single  
  
# Basically we'll keep adding plugins here  
# and leave it up to anyone's trac-admin to enable them after launch  
  
RUN easy_install \  
https://trac-hacks.org/svn/xmlrpcplugin/trunk \  
https://trac-hacks.org/svn/markdownmacro/trunk \  
https://trac-hacks.org/svn/tocmacro/0.11 \  
xlwt https://trac-hacks.org/svn/exceldownloadplugin/0.12 \  
https://trac-hacks.org/svn/icalexporterplugin/0.11/ \  
https://trac-hacks.org/svn/googlecalendarplugin/trunk/ \  
https://trac-hacks.org/svn/navaddplugin/trunk/  
  
# Candidates  
# https://trac-hacks.org/svn/graphvizplugin/trunk/ (with an apt-get)  

