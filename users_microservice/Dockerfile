FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install python3 python3-pip

WORKDIR /app_users
COPY . /app_users

RUN pip3 install -r requirements.txt

#EXPOSE 80

#ENTRYPOINT ["python3"]
#CMD ["views.py"]

