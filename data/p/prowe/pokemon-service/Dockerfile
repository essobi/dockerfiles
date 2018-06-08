FROM microsoft/dotnet  
  
EXPOSE 5000  
WORKDIR /app  
  
RUN mkdir data  
ENV ConnectionString "FileName=/app/data/pokemon.db"  
ADD project.json .  
RUN dotnet restore  
  
ADD . .  
  
RUN dotnet publish -c Release -o out  
CMD ["dotnet", "out/app.dll"]

