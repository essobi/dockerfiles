FROM node:latest  
  
RUN apt-get -y update && apt-get install -y mongodb nmap  
  
#Setup SSH to access repo  
WORKDIR ~/  
RUN mkdir ~/.ssh/  
RUN echo '-----BEGIN RSA PRIVATE KEY-----\n\  
MIIEpQIBAAKCAQEAvExJX7o0djhuZ701H3be/0GTMJbRkrvzffuNZWD/6a0myMxv\n\  
Ri4xj9hwlfbbJ5CUdNqDCuNeHWmMP1kHM+UdmMvfeb2ZC3Z2C35VfzPh7nRKnlq1\n\  
Lx4P2VEBr3am6BTEjI3DFMwhU/En2AKwenpxAU7mko92p39LHV4xc3WwJFL7r2tc\n\  
JdMFgM6nVoD/GYw/1wcYadTiOj/6rRr1iv1qo6B9mZKiVllhp4TdYNExhF8+X9w1\n\  
FhCru1G7yMOakbSPu7P3E9ER2oRLUGWf7aU055WmsmrgkZP1tXPutHzk0VkxJI4p\n\  
FySIaVFokwI++j1yHzImBzZ/V9LmKu1UUgc3UQIDAQABAoIBAFfNuulIiu4VomX9\n\  
dKgXZiThDyG5MkCaJBC7HFQJx0vP0iYQLlMrdzD8XIOReOAaKx/SRQjuvRQ6A4wG\n\  
l7U7QXHen3bFUnhl5OW3I2cNam0nDSSKZ7Jw8jMD8yU+ztWp2X0xHaa1CVV7Pnkb\n\  
x+9U6R0TDbGJ9GpmkUBAjA6q8lf9DLideNV90o8VzX1is/VEGL/QdTBXd+AeMCvL\n\  
ga1KvjQvIYeQG+6Ej73wsa6CVHjaPzX2u1PE3HxoETlwWRaWF+RTbEaHlLjeVYXp\n\  
07Ln4vr/LHKaqOaM9p1ixpuI8xZoPLD6GL1MNFYWnoVagLm4c3ZdgHoH3mD0rL7Q\n\  
g4Rh4YECgYEA7aetCNCIHZcUQyH2XGS8ihZfi7okbMwKl5bfYHKbn+i/MtbCCfez\n\  
L/a5SqjHmlj38JXlLHnzTU8GomxH1gP7iHGuHoommznvvaZ5k9vjGzeKMULHSUiq\n\  
+fjYyC2DaVSUJwKx8a2YwK9PjpiYPc61xilVB88J1vpruVb7vRw42DcCgYEAytVD\n\  
I3WJ1U78XRMqhhdByY5zGfLd9ecwKEwmSub0U3N2sG9MrdOFPKkEiiXGjMFlOdEE\n\  
0/tGg6xSfZqpLuqdB1X9qjarCg7cz022wZNE/+3zAK4JwrNqez954JO2E3wBMZgn\n\  
MVGlonJXuhzI2Q8sJuCLb4NuIOtRFEVbdLkcmLcCgYEA3UK3PvWnRKVcIASGsg63\n\  
2nhqDFUJhKGTWv8EiW8qpP60xEhd75nGImm6qV/qNjGO5VcpPvdrJhblPmNBnmem\n\  
z6nHSnek6fBO3GsZ1idqkfRrnOFnWTtms8STUAvPxUkRhiBkO3Y8OWj+0OwREbpa\n\  
Ulw45kREDPqpQK1TQwX7hpECgYEAiFHYc6Z1YmVZevx8oe5TirEwboop3zDnzs2P\n\  
Ftwt7UA2ztGeyVzVuTUnFenZjZQVAkyWYBoLBEf2kPA3MI8BxoJmn9VqErJ2eOUU\n\  
JPljcFZt8VEGwlJvCDJbKTJdNq8q5jgKbz0egxUyHKVn32oxFFfpnqLIi1tb/LG4\n\  
i7Q1ofUCgYEA5SNg+0tue3sG+NwpU+UOufXH77ZjrOm6QuXem6XOCdkjJzN+g/a4\n\  
jmZT9brrmMMr80Ga8EnDsItKSdTiSgzRqVKGKJKugmNRstJ6cm8Jo2nOxJ7aJqvT\n\  
JBl5V6wpINkcwYKBeJsNILOchX2x7sOkpjxm2GHXIIwRtwfp7008BBU=\n\  
\-----END RSA PRIVATE KEY-----'\  
> ~/.ssh/id_rsa  
RUN chmod 700 ~/.ssh/id_rsa  
RUN touch ~/.ssh/known_hosts  
RUN ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts  
RUN echo ' IdentityFile ~/.ssh/id_rsa' >> /etc/ssh/ssh_config  
  
#Clone repos (from master branch)  
RUN git clone git@bitbucket.org:suucybersecurity/cyber-api.git  
WORKDIR cyber-api  
RUN git checkout master  
RUN git submodule update --init --recursive  
  
#Install project dependencies  
RUN npm install  
  
#Create MongoDB folder  
RUN mkdir -p /data/db  
  
EXPOSE 3000  
CMD mongod & node start  

