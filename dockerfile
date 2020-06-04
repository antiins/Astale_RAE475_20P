FROM python:latest
<<<<<<< HEAD

ADD clienttelnet.yml /client/

WORKDIR /client/ 

=======
ADD servertelnet.yml /server/

WORKDIR /server/
EXPOSE 1234
>>>>>>> TELNET serveris
