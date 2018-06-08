FROM microsoft/dotnet:1.0.0-preview2-sdk  
  
RUN wget -qO- https://github.com/manabedaiki/SplitDiff/archive/master.tar.gz
>/tmp/SplitDiff-master.tar.gz \  
&& tar zxf /tmp/SplitDiff-master.tar.gz -C /tmp \  
&& mv /tmp/SplitDiff-master /tmp/SplitDiff \  
&& dotnet restore /tmp/SplitDiff \  
&& dotnet publish /tmp/SplitDiff \--configuration Release \--output /SplitDiff
\  
&& rm -rf /tmp/SplitDiff-master.tar.gz \  
&& rm -rf /tmp/SplitDiff \  
&& rm -rf /root/.local  

