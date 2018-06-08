FROM mono  
  
RUN ln -sf /bin/bash /bin/sh \  
&& apt-get update \  
&& apt-get install -y \  
git \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD . /codeformatter  
  
RUN cd codeformatter \  
&& sh init-tools.sh \  
&& nuget restore src/CodeFormatter.sln  
  
RUN /codeformatter/src/ExternalApis/msbuild/msbuild
/codeformatter/src/CodeFormatter.sln; exit 0  
  
VOLUME /code  
WORKDIR /code  
  
CMD mono /codeformatter/bin/CodeFormatter/Debug/CodeFormatter.exe
/rule-:NewLineAbove,UnicodeLiterals codeformatter.csproj  

