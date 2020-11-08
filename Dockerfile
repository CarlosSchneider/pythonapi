FROM python
VOLUME ["/var/api", "/var/api/log"]
WORKDIR "/var/api"
COPY ["./requirements.txt", "requirements.txt"]
COPY ["./students_api.py", "students_api.py"]
COPY ["./README.md", "README.md"]
RUN apt-get update -y
RUN pip install -r requirements.txt
EXPOSE 5005/tcp
ENTRYPOINT [ "python3", "students_api.py" ]

