FROM microsoft/dotnet:1.1.1-runtime  
  
RUN mkdir -p /bjd \  
&& cd /bjd \  
&& curl -SL
https://vnextyappveyordeploy.blob.core.windows.net/appveyor/archive/Bjd.CoreCLR.tar.gz
--output Bjd.CoreCLR.tar.gz \  
&& tar -zxf Bjd.CoreCLR.tar.gz -C /bjd \  
&& rm Bjd.CoreCLR.tar.gz  
  
WORKDIR /bjd/publish  
  
ENTRYPOINT ["dotnet", "Bjd.Startup.dll", "--console"]  
  
EXPOSE 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
2024 2025 2026 2027 2028 2029 2030 3021 3025 3053 3067 3069 3080 3110 5050
5060 8021 8023 8025 8080 8090 8110  

